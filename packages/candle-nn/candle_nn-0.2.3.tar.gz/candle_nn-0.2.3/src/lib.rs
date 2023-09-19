#![allow(clippy::redundant_closure_call)]
use pyo3::exceptions::{PyTypeError, PyValueError};
use pyo3::prelude::*;
use pyo3::types::{IntoPyDict, PyDict, PyTuple};
use pyo3::ToPyObject;
use std::sync::Arc;

use half::{bf16, f16};

use ::candle::{quantized::QTensor, DType, Device, Tensor, WithDType};

pub fn wrap_err(err: ::candle::Error) -> PyErr {
    PyErr::new::<PyValueError, _>(format!("{err:?}"))
}

#[derive(Clone, Debug)]
struct PyShape(Vec<usize>);

impl<'source> pyo3::FromPyObject<'source> for PyShape {
    fn extract(ob: &'source PyAny) -> PyResult<Self> {
        let dims: Vec<usize> = pyo3::FromPyObject::extract(ob)?;
        Ok(PyShape(dims))
    }
}

impl From<PyShape> for ::candle::Shape {
    fn from(val: PyShape) -> Self {
        val.0.into()
    }
}

#[derive(Clone, Debug)]
#[pyclass(name = "Tensor")]
/// A `candle` tensor.
struct PyTensor(Tensor);

impl std::ops::Deref for PyTensor {
    type Target = Tensor;

    fn deref(&self) -> &Self::Target {
        &self.0
    }
}

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
#[pyclass(name = "DType")]
/// A `candle` dtype.
struct PyDType(DType);

#[pymethods]
impl PyDType {
    fn __repr__(&self) -> String {
        format!("{:?}", self.0)
    }

    fn __str__(&self) -> String {
        self.__repr__()
    }
}

impl PyDType {
    fn from_pyobject(ob: PyObject, py: Python<'_>) -> PyResult<Self> {
        use std::str::FromStr;
        if let Ok(dtype) = ob.extract::<&str>(py) {
            let dtype = DType::from_str(dtype)
                .map_err(|_| PyTypeError::new_err(format!("invalid dtype '{dtype}'")))?;
            Ok(Self(dtype))
        } else {
            ob.extract(py)
        }
    }
}

static CUDA_DEVICE: std::sync::Mutex<Option<Device>> = std::sync::Mutex::new(None);

#[derive(Clone, Copy, Debug, PartialEq, Eq)]
enum PyDevice {
    Cpu,
    Cuda,
}

impl PyDevice {
    fn from_device(device: &Device) -> Self {
        match device {
            Device::Cpu => Self::Cpu,
            Device::Cuda(_) => Self::Cuda,
        }
    }

    fn as_device(&self) -> PyResult<Device> {
        match self {
            Self::Cpu => Ok(Device::Cpu),
            Self::Cuda => {
                let mut device = CUDA_DEVICE.lock().unwrap();
                if let Some(device) = device.as_ref() {
                    return Ok(device.clone());
                };
                let d = Device::new_cuda(0).map_err(wrap_err)?;
                *device = Some(d.clone());
                Ok(d)
            }
        }
    }
}

impl<'source> FromPyObject<'source> for PyDevice {
    fn extract(ob: &'source PyAny) -> PyResult<Self> {
        let device: &str = ob.extract()?;
        let device = match device {
            "cpu" => PyDevice::Cpu,
            "cuda" => PyDevice::Cuda,
            _ => Err(PyTypeError::new_err(format!("invalid device '{device}'")))?,
        };
        Ok(device)
    }
}

impl ToPyObject for PyDevice {
    fn to_object(&self, py: Python<'_>) -> PyObject {
        let str = match self {
            PyDevice::Cpu => "cpu",
            PyDevice::Cuda => "cuda",
        };
        str.to_object(py)
    }
}

trait PyWithDType: WithDType {
    fn to_py(&self, py: Python<'_>) -> PyObject;
}

macro_rules! pydtype {
    ($ty:ty, $conv:expr) => {
        impl PyWithDType for $ty {
            fn to_py(&self, py: Python<'_>) -> PyObject {
                $conv(*self).to_object(py)
            }
        }
    };
}
pydtype!(u8, |v| v);
pydtype!(u32, |v| v);
pydtype!(i64, |v| v);
pydtype!(f16, f32::from);
pydtype!(bf16, f32::from);
pydtype!(f32, |v| v);
pydtype!(f64, |v| v);

fn actual_index(t: &Tensor, dim: usize, index: i64) -> ::candle::Result<usize> {
    let dim = t.dim(dim)?;
    if 0 <= index {
        let index = index as usize;
        if dim <= index {
            ::candle::bail!("index {index} is too large for tensor dimension {dim}")
        }
        Ok(index)
    } else {
        if (dim as i64) < -index {
            ::candle::bail!("index {index} is too low for tensor dimension {dim}")
        }
        Ok((dim as i64 + index) as usize)
    }
}

fn actual_dim(t: &Tensor, dim: i64) -> ::candle::Result<usize> {
    let rank = t.rank();
    if 0 <= dim {
        let dim = dim as usize;
        if rank <= dim {
            ::candle::bail!("dimension index {dim} is too large for tensor rank {rank}")
        }
        Ok(dim)
    } else {
        if (rank as i64) < -dim {
            ::candle::bail!("dimension index {dim} is too low for tensor rank {rank}")
        }
        Ok((rank as i64 + dim) as usize)
    }
}

// TODO: Something similar to this should probably be a part of candle core.
trait MapDType {
    type Output;
    fn f<T: PyWithDType>(&self, t: &Tensor) -> PyResult<Self::Output>;

    fn map(&self, t: &Tensor) -> PyResult<Self::Output> {
        match t.dtype() {
            DType::U8 => self.f::<u8>(t),
            DType::U32 => self.f::<u32>(t),
            DType::I64 => self.f::<i64>(t),
            DType::BF16 => self.f::<bf16>(t),
            DType::F16 => self.f::<f16>(t),
            DType::F32 => self.f::<f32>(t),
            DType::F64 => self.f::<f64>(t),
        }
    }
}

#[pymethods]
impl PyTensor {
    #[new]
    #[pyo3(text_signature = "(self, data:_ArrayLike)")]
    // TODO: Handle arbitrary input dtype and shape.
    /// Creates a new tensor from a Python value. The value can be a scalar or array-like object.
    fn new(py: Python<'_>, data: PyObject) -> PyResult<Self> {
        use Device::Cpu;
        let tensor = if let Ok(vs) = data.extract::<u32>(py) {
            Tensor::new(vs, &Cpu).map_err(wrap_err)?
        } else if let Ok(vs) = data.extract::<i64>(py) {
            Tensor::new(vs, &Cpu).map_err(wrap_err)?
        } else if let Ok(vs) = data.extract::<f32>(py) {
            Tensor::new(vs, &Cpu).map_err(wrap_err)?
        } else if let Ok(vs) = data.extract::<Vec<u32>>(py) {
            let len = vs.len();
            Tensor::from_vec(vs, len, &Cpu).map_err(wrap_err)?
        } else if let Ok(vs) = data.extract::<Vec<i64>>(py) {
            let len = vs.len();
            Tensor::from_vec(vs, len, &Cpu).map_err(wrap_err)?
        } else if let Ok(vs) = data.extract::<Vec<f32>>(py) {
            let len = vs.len();
            Tensor::from_vec(vs, len, &Cpu).map_err(wrap_err)?
        } else if let Ok(vs) = data.extract::<Vec<Vec<u32>>>(py) {
            Tensor::new(vs, &Cpu).map_err(wrap_err)?
        } else if let Ok(vs) = data.extract::<Vec<Vec<i64>>>(py) {
            Tensor::new(vs, &Cpu).map_err(wrap_err)?
        } else if let Ok(vs) = data.extract::<Vec<Vec<f32>>>(py) {
            Tensor::new(vs, &Cpu).map_err(wrap_err)?
        } else if let Ok(vs) = data.extract::<Vec<Vec<Vec<u32>>>>(py) {
            Tensor::new(vs, &Cpu).map_err(wrap_err)?
        } else if let Ok(vs) = data.extract::<Vec<Vec<Vec<i64>>>>(py) {
            Tensor::new(vs, &Cpu).map_err(wrap_err)?
        } else if let Ok(vs) = data.extract::<Vec<Vec<Vec<f32>>>>(py) {
            Tensor::new(vs, &Cpu).map_err(wrap_err)?
        } else {
            let ty = data.as_ref(py).get_type();
            Err(PyTypeError::new_err(format!(
                "incorrect type {ty} for tensor"
            )))?
        };
        Ok(Self(tensor))
    }

    /// Gets the tensor's data as a Python scalar or array-like object.
    /// &RETURNS&: _ArrayLike
    fn values(&self, py: Python<'_>) -> PyResult<PyObject> {
        struct M<'a>(Python<'a>);
        impl<'a> MapDType for M<'a> {
            type Output = PyObject;
            fn f<T: PyWithDType>(&self, t: &Tensor) -> PyResult<Self::Output> {
                match t.rank() {
                    0 => Ok(t.to_scalar::<T>().map_err(wrap_err)?.to_py(self.0)),
                    1 => {
                        let v = t.to_vec1::<T>().map_err(wrap_err)?;
                        let v = v.iter().map(|v| v.to_py(self.0)).collect::<Vec<_>>();
                        Ok(v.to_object(self.0))
                    }
                    2 => {
                        let v = t.to_vec2::<T>().map_err(wrap_err)?;
                        let v = v
                            .iter()
                            .map(|v| v.iter().map(|v| v.to_py(self.0)).collect())
                            .collect::<Vec<Vec<_>>>();
                        Ok(v.to_object(self.0))
                    }
                    3 => {
                        let v = t.to_vec3::<T>().map_err(wrap_err)?;
                        let v = v
                            .iter()
                            .map(|v| {
                                v.iter()
                                    .map(|v| v.iter().map(|v| v.to_py(self.0)).collect())
                                    .collect()
                            })
                            .collect::<Vec<Vec<Vec<_>>>>();
                        Ok(v.to_object(self.0))
                    }
                    n => Err(PyTypeError::new_err(format!(
                        "TODO: conversion to PyObject is not handled for rank {n}"
                    )))?,
                }
            }
        }
        // TODO: Handle arbitrary shapes.
        M(py).map(self)
    }

    #[getter]
    /// Gets the tensor's shape.
    /// &RETURNS&: Tuple[int]
    fn shape(&self, py: Python<'_>) -> PyObject {
        PyTuple::new(py, self.0.dims()).to_object(py)
    }

    #[getter]
    /// Gets the tensor's strides.
    /// &RETURNS&: Tuple[int]
    fn stride(&self, py: Python<'_>) -> PyObject {
        PyTuple::new(py, self.0.stride()).to_object(py)
    }

    #[getter]
    /// Gets the tensor's dtype.
    /// &RETURNS&: DType
    fn dtype(&self) -> PyDType {
        PyDType(self.0.dtype())
    }

    #[getter]
    /// Gets the tensor's device.
    /// &RETURNS&: Device
    fn device(&self, py: Python<'_>) -> PyObject {
        PyDevice::from_device(self.0.device()).to_object(py)
    }

    #[getter]
    /// Gets the tensor's rank.
    /// &RETURNS&: int
    fn rank(&self) -> usize {
        self.0.rank()
    }

    fn __repr__(&self) -> String {
        format!("{}", self.0)
    }

    fn __str__(&self) -> String {
        self.__repr__()
    }

    /// Performs the `sin` operation on the tensor.
    /// &RETURNS&: Tensor
    fn sin(&self) -> PyResult<Self> {
        Ok(PyTensor(self.0.sin().map_err(wrap_err)?))
    }

    /// Performs the `cos` operation on the tensor.
    /// &RETURNS&: Tensor
    fn cos(&self) -> PyResult<Self> {
        Ok(PyTensor(self.0.cos().map_err(wrap_err)?))
    }

    /// Performs the `log` operation on the tensor.
    /// &RETURNS&: Tensor
    fn log(&self) -> PyResult<Self> {
        Ok(PyTensor(self.0.log().map_err(wrap_err)?))
    }

    /// Squares the tensor.
    /// &RETURNS&: Tensor
    fn sqr(&self) -> PyResult<Self> {
        Ok(PyTensor(self.0.sqr().map_err(wrap_err)?))
    }

    /// Calculates the square root of the tensor.
    /// &RETURNS&: Tensor
    fn sqrt(&self) -> PyResult<Self> {
        Ok(PyTensor(self.0.sqrt().map_err(wrap_err)?))
    }

    /// Get the `recip` of the tensor.
    /// &RETURNS&: Tensor
    fn recip(&self) -> PyResult<Self> {
        Ok(PyTensor(self.0.recip().map_err(wrap_err)?))
    }

    /// Performs the `exp` operation on the tensor.
    /// &RETURNS&: Tensor
    fn exp(&self) -> PyResult<Self> {
        Ok(PyTensor(self.0.exp().map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, p:float)")]
    /// Performs the `pow` operation on the tensor with the given exponent.
    /// &RETURNS&: Tensor
    fn powf(&self, p: f64) -> PyResult<Self> {
        Ok(PyTensor(self.0.powf(p).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, rhs:Tensor, dim:int)")]
    /// Select values for the input tensor at the target indexes across the specified dimension.
    ///
    /// The `indexes` is argument is an int tensor with a single dimension.
    /// The output has the same number of dimension as the `self` input. The target dimension of
    /// the output has length the length of `indexes` and the values are taken from `self` using
    /// the index from `indexes`. Other dimensions have the same number of elements as the input
    /// tensor.
    /// &RETURNS&: Tensor
    fn index_select(&self, rhs: &Self, dim: i64) -> PyResult<Self> {
        let dim = actual_dim(self, dim).map_err(wrap_err)?;
        Ok(PyTensor(self.0.index_select(rhs, dim).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, rhs:Tensor)")]
    /// Performs a matrix multiplication between the two tensors.
    /// &RETURNS&: Tensor
    fn matmul(&self, rhs: &Self) -> PyResult<Self> {
        Ok(PyTensor(self.0.matmul(rhs).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, rhs:Tensor)")]
    /// Adds the two tensors, while broadcasting the right-hand-side tensor to match the shape of the left-hand-side tensor.
    /// &RETURNS&: Tensor
    fn broadcast_add(&self, rhs: &Self) -> PyResult<Self> {
        Ok(PyTensor(self.0.broadcast_add(rhs).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, rhs:Tensor)")]
    /// Subtracts the two tensors, while broadcasting the right-hand-side tensor to match the shape of the left-hand-side tensor.
    /// &RETURNS&: Tensor
    fn broadcast_sub(&self, rhs: &Self) -> PyResult<Self> {
        Ok(PyTensor(self.0.broadcast_sub(rhs).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, rhs:Tensor)")]
    /// Multiplies the two tensors, while broadcasting the right-hand-side tensor to match the shape of the left-hand-side tensor.
    /// &RETURNS&: Tensor
    fn broadcast_mul(&self, rhs: &Self) -> PyResult<Self> {
        Ok(PyTensor(self.0.broadcast_mul(rhs).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, rhs:Tensor)")]
    /// Divides the two tensors, while broadcasting the right-hand-side tensor to match the shape of the left-hand-side tensor.
    /// &RETURNS&: Tensor
    fn broadcast_div(&self, rhs: &Self) -> PyResult<Self> {
        Ok(PyTensor(self.0.broadcast_div(rhs).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, on_true:Tensor, on_false:Tensor)")]
    /// Returns a tensor with the same shape as the input tensor, the values are taken from
    /// `on_true` if the input tensor value is not zero, and `on_false` at the positions where the
    /// input tensor is equal to zero.
    /// &RETURNS&: Tensor
    fn where_cond(&self, on_true: &Self, on_false: &Self) -> PyResult<Self> {
        Ok(PyTensor(
            self.0.where_cond(on_true, on_false).map_err(wrap_err)?,
        ))
    }

    /// Add two tensors.
    /// &RETURNS&: Tensor
    fn __add__(&self, rhs: &PyAny) -> PyResult<Self> {
        let tensor = if let Ok(rhs) = rhs.extract::<Self>() {
            (&self.0 + &rhs.0).map_err(wrap_err)?
        } else if let Ok(rhs) = rhs.extract::<f64>() {
            (&self.0 + rhs).map_err(wrap_err)?
        } else {
            Err(PyTypeError::new_err("unsupported rhs for add"))?
        };
        Ok(Self(tensor))
    }

    fn __radd__(&self, rhs: &PyAny) -> PyResult<Self> {
        self.__add__(rhs)
    }

    /// Multiply two tensors.
    /// &RETURNS&: Tensor
    fn __mul__(&self, rhs: &PyAny) -> PyResult<Self> {
        let tensor = if let Ok(rhs) = rhs.extract::<Self>() {
            (&self.0 * &rhs.0).map_err(wrap_err)?
        } else if let Ok(rhs) = rhs.extract::<f64>() {
            (&self.0 * rhs).map_err(wrap_err)?
        } else {
            Err(PyTypeError::new_err("unsupported rhs for mul"))?
        };
        Ok(Self(tensor))
    }

    fn __rmul__(&self, rhs: &PyAny) -> PyResult<Self> {
        self.__mul__(rhs)
    }

    /// Subtract two tensors.
    /// &RETURNS&: Tensor
    fn __sub__(&self, rhs: &PyAny) -> PyResult<Self> {
        let tensor = if let Ok(rhs) = rhs.extract::<Self>() {
            (&self.0 - &rhs.0).map_err(wrap_err)?
        } else if let Ok(rhs) = rhs.extract::<f64>() {
            (&self.0 - rhs).map_err(wrap_err)?
        } else {
            Err(PyTypeError::new_err("unsupported rhs for sub"))?
        };
        Ok(Self(tensor))
    }

    /// Divide two tensors.
    /// &RETURNS&: Tensor
    fn __truediv__(&self, rhs: &PyAny) -> PyResult<Self> {
        let tensor = if let Ok(rhs) = rhs.extract::<Self>() {
            (&self.0 / &rhs.0).map_err(wrap_err)?
        } else if let Ok(rhs) = rhs.extract::<f64>() {
            (&self.0 / rhs).map_err(wrap_err)?
        } else {
            Err(PyTypeError::new_err("unsupported rhs for div"))?
        };
        Ok(Self(tensor))
    }

    #[pyo3(text_signature = "(self, shape:Sequence[int])")]
    /// Reshapes the tensor to the given shape.
    /// &RETURNS&: Tensor
    fn reshape(&self, shape: PyShape) -> PyResult<Self> {
        Ok(PyTensor(self.0.reshape(shape).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, shape:Sequence[int])")]
    /// Broadcasts the tensor to the given shape.
    /// &RETURNS&: Tensor
    fn broadcast_as(&self, shape: PyShape) -> PyResult<Self> {
        Ok(PyTensor(self.0.broadcast_as(shape).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, shape:Sequence[int])")]
    /// Broadcasts the tensor to the given shape, adding new dimensions on the left.
    /// &RETURNS&: Tensor
    fn broadcast_left(&self, shape: PyShape) -> PyResult<Self> {
        Ok(PyTensor(self.0.broadcast_left(shape).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, dim:int)")]
    /// Creates a new tensor with the specified dimension removed if its size was one.
    /// &RETURNS&: Tensor
    fn squeeze(&self, dim: i64) -> PyResult<Self> {
        let dim = actual_dim(self, dim).map_err(wrap_err)?;
        Ok(PyTensor(self.0.squeeze(dim).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, dim:int)")]
    /// Creates a new tensor with a dimension of size one inserted at the specified position.
    /// &RETURNS&: Tensor
    fn unsqueeze(&self, dim: usize) -> PyResult<Self> {
        Ok(PyTensor(self.0.unsqueeze(dim).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, index:int)")]
    /// Gets the value at the specified index.
    /// &RETURNS&: Tensor
    fn get(&self, index: i64) -> PyResult<Self> {
        let index = actual_index(self, 0, index).map_err(wrap_err)?;
        Ok(PyTensor(self.0.get(index).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, dim1:int, dim2:int)")]
    /// Returns a tensor that is a transposed version of the input, the given dimensions are swapped.
    /// &RETURNS&: Tensor
    fn transpose(&self, dim1: usize, dim2: usize) -> PyResult<Self> {
        Ok(PyTensor(self.0.transpose(dim1, dim2).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, dim:int, start:int, len:int)")]
    /// Returns a new tensor that is a narrowed version of the input, the dimension `dim`
    /// ranges from `start` to `start + len`.
    /// &RETURNS&: Tensor
    fn narrow(&self, dim: i64, start: i64, len: usize) -> PyResult<Self> {
        let dim = actual_dim(self, dim).map_err(wrap_err)?;
        let start = actual_index(self, dim, start).map_err(wrap_err)?;
        Ok(PyTensor(self.0.narrow(dim, start, len).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, dim:int)")]
    /// Returns the indices of the maximum value(s) across the selected dimension.
    /// &RETURNS&: Tensor
    fn argmax_keepdim(&self, dim: i64) -> PyResult<Self> {
        let dim = actual_dim(self, dim).map_err(wrap_err)?;
        Ok(PyTensor(self.0.argmax_keepdim(dim).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, dim:int)")]
    /// Returns the indices of the minimum value(s) across the selected dimension.
    /// &RETURNS&: Tensor
    fn argmin_keepdim(&self, dim: i64) -> PyResult<Self> {
        let dim = actual_dim(self, dim).map_err(wrap_err)?;
        Ok(PyTensor(self.0.argmin_keepdim(dim).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, dim:int)")]
    /// Gathers the maximum value across the selected dimension.
    /// &RETURNS&: Tensor
    fn max_keepdim(&self, dim: i64) -> PyResult<Self> {
        let dim = actual_dim(self, dim).map_err(wrap_err)?;
        Ok(PyTensor(self.0.max_keepdim(dim).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, dim:int)")]
    /// Gathers the minimum value across the selected dimension.
    /// &RETURNS&: Tensor
    fn min_keepdim(&self, dim: i64) -> PyResult<Self> {
        let dim = actual_dim(self, dim).map_err(wrap_err)?;
        Ok(PyTensor(self.0.min_keepdim(dim).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, dim:Union[int, List[int]])")]
    /// Returns the sum of all elements in the input tensor. The sum is performed over all the input dimensions.
    /// &RETURNS&: Tensor
    fn sum_keepdim(&self, dims: PyObject, py: Python<'_>) -> PyResult<Self> {
        let dims = if let Ok(dim) = dims.extract::<usize>(py) {
            vec![dim]
        } else {
            dims.extract::<Vec<usize>>(py)?
        };
        Ok(PyTensor(
            self.0.sum_keepdim(dims.as_slice()).map_err(wrap_err)?,
        ))
    }

    /// Returns the sum of the tensor.
    /// &RETURNS&: Tensor
    fn sum_all(&self) -> PyResult<Self> {
        Ok(PyTensor(self.0.sum_all().map_err(wrap_err)?))
    }

    /// Returns the mean of the tensor.
    /// &RETURNS&: Tensor
    fn mean_all(&self) -> PyResult<Self> {
        let elements = self.0.elem_count();
        let sum = self.0.sum_all().map_err(wrap_err)?;
        let mean = (sum / elements as f64).map_err(wrap_err)?;
        Ok(PyTensor(mean))
    }

    #[pyo3(text_signature = "(self, dim:int)")]
    /// Flattens the tensor on the dimension indexes from `dim` (inclusive) to the last dimension.
    /// &RETURNS&: Tensor
    fn flatten_from(&self, dim: i64) -> PyResult<Self> {
        let dim = actual_dim(self, dim).map_err(wrap_err)?;
        Ok(PyTensor(self.0.flatten_from(dim).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, dim:int)")]
    ///Flattens the tensor on the dimension indexes from `0` to `dim` (inclusive).
    /// &RETURNS&: Tensor
    fn flatten_to(&self, dim: i64) -> PyResult<Self> {
        let dim = actual_dim(self, dim).map_err(wrap_err)?;
        Ok(PyTensor(self.0.flatten_to(dim).map_err(wrap_err)?))
    }

    /// Flattens the tensor into a 1D tensor.
    /// &RETURNS&: Tensor
    fn flatten_all(&self) -> PyResult<Self> {
        Ok(PyTensor(self.0.flatten_all().map_err(wrap_err)?))
    }

    /// Transposes the tensor.
    /// &RETURNS&: Tensor
    fn t(&self) -> PyResult<Self> {
        Ok(PyTensor(self.0.t().map_err(wrap_err)?))
    }

    /// Makes the tensor contiguous in memory.
    /// &RETURNS&: Tensor
    fn contiguous(&self) -> PyResult<Self> {
        Ok(PyTensor(self.0.contiguous().map_err(wrap_err)?))
    }

    /// Returns true if the tensor is contiguous in C order.
    /// &RETURNS&: bool
    fn is_contiguous(&self) -> bool {
        self.0.is_contiguous()
    }

    /// Returns true if the tensor is contiguous in Fortran order.
    /// &RETURNS&: bool
    fn is_fortran_contiguous(&self) -> bool {
        self.0.is_fortran_contiguous()
    }

    /// Detach the tensor from the computation graph.
    /// &RETURNS&: Tensor
    fn detach(&self) -> PyResult<Self> {
        Ok(PyTensor(self.0.detach().map_err(wrap_err)?))
    }

    /// Returns a copy of the tensor.
    /// &RETURNS&: Tensor
    fn copy(&self) -> PyResult<Self> {
        Ok(PyTensor(self.0.copy().map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, dtype:Union[str,DType])")]
    /// Convert the tensor to a new dtype.
    /// &RETURNS&: Tensor
    fn to_dtype(&self, dtype: PyObject, py: Python<'_>) -> PyResult<Self> {
        let dtype = PyDType::from_pyobject(dtype, py)?;
        Ok(PyTensor(self.0.to_dtype(dtype.0).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, device:Union[str,Device])")]
    /// Move the tensor to a new device.
    /// &RETURNS&: Tensor
    fn to_device(&self, device: PyDevice) -> PyResult<Self> {
        let device = device.as_device()?;
        Ok(PyTensor(self.0.to_device(&device).map_err(wrap_err)?))
    }

    #[pyo3(text_signature = "(self, quantized_dtype:str)")]
    /// Quantize the tensor.
    /// &RETURNS&: QTensor
    fn quantize(&self, quantized_dtype: &str) -> PyResult<PyQTensor> {
        use ::candle::quantized;
        let res = match quantized_dtype {
            "q2k" => quantized::QTensor::quantize::<quantized::k_quants::BlockQ2K>(self),
            "q3k" => quantized::QTensor::quantize::<quantized::k_quants::BlockQ3K>(self),
            "q4_0" => quantized::QTensor::quantize::<quantized::k_quants::BlockQ4_0>(self),
            "q4_1" => quantized::QTensor::quantize::<quantized::k_quants::BlockQ4_1>(self),
            "q4k" => quantized::QTensor::quantize::<quantized::k_quants::BlockQ4K>(self),
            "q5_0" => quantized::QTensor::quantize::<quantized::k_quants::BlockQ5_0>(self),
            "q5_1" => quantized::QTensor::quantize::<quantized::k_quants::BlockQ5_1>(self),
            "q5k" => quantized::QTensor::quantize::<quantized::k_quants::BlockQ5K>(self),
            "q6k" => quantized::QTensor::quantize::<quantized::k_quants::BlockQ6K>(self),
            "q8_0" => quantized::QTensor::quantize::<quantized::k_quants::BlockQ8_0>(self),
            "q8_1" => quantized::QTensor::quantize::<quantized::k_quants::BlockQ8_1>(self),
            "q8k" => quantized::QTensor::quantize::<quantized::k_quants::BlockQ8K>(self),
            "f16" => quantized::QTensor::quantize::<f16>(self),
            "f32" => quantized::QTensor::quantize::<f32>(self),
            dt => {
                return Err(PyErr::new::<PyValueError, _>(format!(
                    "unknown quantized-dtype {dt}"
                )))
            }
        };
        Ok(PyQTensor(Arc::new(res.map_err(wrap_err)?)))
    }
}

#[pyfunction]
#[pyo3(text_signature = "(tensors:List[Tensor], dim:int )")]
/// Concatenate the tensors across one axis.
/// &RETURNS&: Tensor
fn cat(tensors: Vec<PyTensor>, dim: i64) -> PyResult<PyTensor> {
    if tensors.is_empty() {
        return Err(PyErr::new::<PyValueError, _>("empty input to cat"));
    }
    let dim = actual_dim(&tensors[0], dim).map_err(wrap_err)?;
    let tensors = tensors.into_iter().map(|t| t.0).collect::<Vec<_>>();
    let tensor = Tensor::cat(&tensors, dim).map_err(wrap_err)?;
    Ok(PyTensor(tensor))
}

#[pyfunction]
#[pyo3(text_signature = "(tensors:List[Tensor], dim:int)")]
/// Stack the tensors along a new axis.
/// &RETURNS&: Tensor
fn stack(tensors: Vec<PyTensor>, dim: usize) -> PyResult<PyTensor> {
    let tensors = tensors.into_iter().map(|t| t.0).collect::<Vec<_>>();
    let tensor = Tensor::stack(&tensors, dim).map_err(wrap_err)?;
    Ok(PyTensor(tensor))
}

#[pyfunction]
#[pyo3(text_signature = "(data:_ArrayLike)")]
/// Creates a new tensor from a Python value. The value can be a scalar or array-like object.
/// &RETURNS&: Tensor
fn tensor(py: Python<'_>, data: PyObject) -> PyResult<PyTensor> {
    PyTensor::new(py, data)
}

#[pyfunction]
#[pyo3(signature = (shape, *, device=None), text_signature = "(shape:Sequence[int], device:Optional[Device]=None)")]
/// Creates a new tensor with random values.
/// &RETURNS&: Tensor
fn rand(_py: Python<'_>, shape: PyShape, device: Option<PyDevice>) -> PyResult<PyTensor> {
    let device = device.unwrap_or(PyDevice::Cpu).as_device()?;
    let tensor = Tensor::rand(0f32, 1f32, shape.0, &device).map_err(wrap_err)?;
    Ok(PyTensor(tensor))
}

#[pyfunction]
#[pyo3(signature = (shape, *, device=None), text_signature = "(shape:Sequence[int], device:Optional[Device]=None)")]
/// Creates a new tensor with random values from a normal distribution.
/// &RETURNS&: Tensor
fn randn(_py: Python<'_>, shape: PyShape, device: Option<PyDevice>) -> PyResult<PyTensor> {
    let device = device.unwrap_or(PyDevice::Cpu).as_device()?;
    let tensor = Tensor::randn(0f32, 1f32, shape.0, &device).map_err(wrap_err)?;
    Ok(PyTensor(tensor))
}

#[pyfunction]
#[pyo3(signature = (shape, *, dtype=None, device=None),text_signature = "(shape:Sequence[int], dtype:Optional[DType]=None, device:Optional[Device]=None)")]
/// Creates a new tensor filled with ones.
/// &RETURNS&: Tensor
fn ones(
    py: Python<'_>,
    shape: PyShape,
    dtype: Option<PyObject>,
    device: Option<PyDevice>,
) -> PyResult<PyTensor> {
    let dtype = match dtype {
        None => DType::F32,
        Some(dtype) => PyDType::from_pyobject(dtype, py)?.0,
    };
    let device = device.unwrap_or(PyDevice::Cpu).as_device()?;
    let tensor = Tensor::ones(shape.0, dtype, &device).map_err(wrap_err)?;
    Ok(PyTensor(tensor))
}

#[pyfunction]
#[pyo3(signature = (shape, *, dtype=None, device=None), text_signature = "(shape:Sequence[int], dtype:Optional[DType]=None, device:Optional[Device]=None)")]
/// Creates a new tensor filled with zeros.
/// &RETURNS&: Tensor
fn zeros(
    py: Python<'_>,
    shape: PyShape,
    dtype: Option<PyObject>,
    device: Option<PyDevice>,
) -> PyResult<PyTensor> {
    let dtype = match dtype {
        None => DType::F32,
        Some(dtype) => PyDType::from_pyobject(dtype, py)?.0,
    };
    let device = device.unwrap_or(PyDevice::Cpu).as_device()?;
    let tensor = Tensor::zeros(shape.0, dtype, &device).map_err(wrap_err)?;
    Ok(PyTensor(tensor))
}

#[derive(Debug, Clone)]
#[pyclass(name = "QTensor")]
/// A quantized tensor.
struct PyQTensor(Arc<QTensor>);

impl std::ops::Deref for PyQTensor {
    type Target = QTensor;

    fn deref(&self) -> &Self::Target {
        self.0.as_ref()
    }
}

#[pymethods]
impl PyQTensor {
    #[getter]
    ///Gets the tensors quantized dtype.
    /// &RETURNS&: str
    fn ggml_dtype(&self) -> String {
        format!("{:?}", self.0.dtype())
    }

    #[getter]
    ///Gets the rank of the tensor.
    /// &RETURNS&: int
    fn rank(&self) -> usize {
        self.0.rank()
    }

    #[getter]
    ///Gets the shape of the tensor.
    /// &RETURNS&: Tuple[int]
    fn shape(&self, py: Python<'_>) -> PyObject {
        PyTuple::new(py, self.0.shape().dims()).to_object(py)
    }

    fn __repr__(&self) -> String {
        format!("{:?}", self.0)
    }

    fn __str__(&self) -> String {
        self.__repr__()
    }

    /// Dequantizes the tensor.
    /// &RETURNS&: Tensor  
    fn dequantize(&self) -> PyResult<PyTensor> {
        let tensor = self.0.dequantize(&Device::Cpu).map_err(wrap_err)?;
        Ok(PyTensor(tensor))
    }

    #[pyo3(text_signature = "(self, lhs:Tensor)")]
    /// Performs a quantized matrix multiplication, with the quantized tensor as the right hand side.
    /// &RETURNS&: Tensor
    fn matmul_t(&self, lhs: &PyTensor) -> PyResult<PyTensor> {
        let qmatmul = ::candle::quantized::QMatMul::from_arc(self.0.clone());
        let res = qmatmul.forward(lhs).map_err(wrap_err)?;
        Ok(PyTensor(res))
    }
}

#[pyfunction]
#[pyo3(text_signature = "(path:Union[str,PathLike])")]
/// Loads a safetensors file. Returns a dictionary mapping tensor names to tensors.
/// &RETURNS&: Dict[str,Tensor]
fn load_safetensors(path: &str, py: Python<'_>) -> PyResult<PyObject> {
    let res = ::candle::safetensors::load(path, &Device::Cpu).map_err(wrap_err)?;
    let res = res
        .into_iter()
        .map(|(key, value)| (key, PyTensor(value).into_py(py)))
        .collect::<Vec<_>>();
    Ok(res.into_py_dict(py).to_object(py))
}

#[pyfunction]
#[pyo3(text_signature = "(path:Union[str,PathLike], tensors:Dict[str,Tensor])")]
/// Saves a dictionary of tensors to a safetensors file.
/// &RETURNS&: None
fn save_safetensors(
    path: &str,
    tensors: std::collections::HashMap<String, PyTensor>,
) -> PyResult<()> {
    let tensors = tensors
        .into_iter()
        .map(|(s, t)| (s, t.0))
        .collect::<std::collections::HashMap<_, _>>();
    ::candle::safetensors::save(&tensors, path).map_err(wrap_err)
}

#[pyfunction]
#[pyo3(text_signature = "(path:Union[str,PathLike])")]
/// Load a GGML file. Returns a tuple of three objects: a dictionary mapping tensor names to tensors,
/// a dictionary mapping hyperparameter names to hyperparameter values, and a vocabulary.
/// &RETURNS&: Tuple[Dict[str,QTensor], Dict[str,Any], List[str]]
fn load_ggml(path: &str, py: Python<'_>) -> PyResult<(PyObject, PyObject, PyObject)> {
    let mut file = std::fs::File::open(path)?;
    let ggml = ::candle::quantized::ggml_file::Content::read(&mut file).map_err(wrap_err)?;
    let tensors = ggml
        .tensors
        .into_iter()
        .map(|(key, qtensor)| Ok((key, PyQTensor(Arc::new(qtensor)).into_py(py))))
        .collect::<::candle::Result<Vec<_>>>()
        .map_err(wrap_err)?;
    let tensors = tensors.into_py_dict(py).to_object(py);
    let hparams = [
        ("n_vocab", ggml.hparams.n_vocab),
        ("n_embd", ggml.hparams.n_embd),
        ("n_mult", ggml.hparams.n_mult),
        ("n_head", ggml.hparams.n_head),
        ("n_layer", ggml.hparams.n_layer),
        ("n_rot", ggml.hparams.n_rot),
        ("ftype", ggml.hparams.ftype),
    ];
    let hparams = hparams.into_py_dict(py).to_object(py);
    let vocab = ggml
        .vocab
        .token_score_pairs
        .iter()
        .map(|(bytes, _)| String::from_utf8_lossy(bytes.as_slice()).to_string())
        .collect::<Vec<String>>()
        .to_object(py);
    Ok((tensors, hparams, vocab))
}

#[pyfunction]
#[pyo3(text_signature = "(path:Union[str,PathLike])")]
/// Loads a GGUF file. Returns a tuple of two dictionaries: the first maps tensor names to tensors,
/// and the second maps metadata keys to metadata values.
/// &RETURNS&: Tuple[Dict[str,QTensor], Dict[str,Any]]
fn load_gguf(path: &str, py: Python<'_>) -> PyResult<(PyObject, PyObject)> {
    use ::candle::quantized::gguf_file;
    fn gguf_value_to_pyobject(v: &gguf_file::Value, py: Python<'_>) -> PyResult<PyObject> {
        let v: PyObject = match v {
            gguf_file::Value::U8(x) => x.into_py(py),
            gguf_file::Value::I8(x) => x.into_py(py),
            gguf_file::Value::U16(x) => x.into_py(py),
            gguf_file::Value::I16(x) => x.into_py(py),
            gguf_file::Value::U32(x) => x.into_py(py),
            gguf_file::Value::I32(x) => x.into_py(py),
            gguf_file::Value::U64(x) => x.into_py(py),
            gguf_file::Value::I64(x) => x.into_py(py),
            gguf_file::Value::F32(x) => x.into_py(py),
            gguf_file::Value::F64(x) => x.into_py(py),
            gguf_file::Value::Bool(x) => x.into_py(py),
            gguf_file::Value::String(x) => x.into_py(py),
            gguf_file::Value::Array(x) => {
                let list = pyo3::types::PyList::empty(py);
                for elem in x.iter() {
                    list.append(gguf_value_to_pyobject(elem, py)?)?;
                }
                list.into()
            }
        };
        Ok(v)
    }
    let mut file = std::fs::File::open(path)?;
    let gguf = gguf_file::Content::read(&mut file).map_err(wrap_err)?;
    let tensors = gguf
        .tensor_infos
        .keys()
        .map(|key| {
            let qtensor = gguf.tensor(&mut file, key)?;
            Ok((key, PyQTensor(Arc::new(qtensor)).into_py(py)))
        })
        .collect::<::candle::Result<Vec<_>>>()
        .map_err(wrap_err)?;
    let tensors = tensors.into_py_dict(py).to_object(py);
    let metadata = gguf
        .metadata
        .iter()
        .map(|(key, value)| Ok((key, gguf_value_to_pyobject(value, py)?)))
        .collect::<PyResult<Vec<_>>>()?
        .into_py_dict(py)
        .to_object(py);
    Ok((tensors, metadata))
}

#[pyfunction]
#[pyo3(
    text_signature = "(path:Union[str,PathLike], tensors:Dict[str,QTensor], metadata:Dict[str,Any])"
)]
/// Save quanitzed tensors and metadata to a GGUF file.
fn save_gguf(path: &str, tensors: PyObject, metadata: PyObject, py: Python<'_>) -> PyResult<()> {
    use ::candle::quantized::gguf_file;

    fn pyobject_to_gguf_value(v: &PyAny, py: Python<'_>) -> PyResult<gguf_file::Value> {
        let v: gguf_file::Value = if let Ok(x) = v.extract::<u8>() {
            gguf_file::Value::U8(x)
        } else if let Ok(x) = v.extract::<i8>() {
            gguf_file::Value::I8(x)
        } else if let Ok(x) = v.extract::<u16>() {
            gguf_file::Value::U16(x)
        } else if let Ok(x) = v.extract::<i16>() {
            gguf_file::Value::I16(x)
        } else if let Ok(x) = v.extract::<u32>() {
            gguf_file::Value::U32(x)
        } else if let Ok(x) = v.extract::<i32>() {
            gguf_file::Value::I32(x)
        } else if let Ok(x) = v.extract::<u64>() {
            gguf_file::Value::U64(x)
        } else if let Ok(x) = v.extract::<i64>() {
            gguf_file::Value::I64(x)
        } else if let Ok(x) = v.extract::<f32>() {
            gguf_file::Value::F32(x)
        } else if let Ok(x) = v.extract::<f64>() {
            gguf_file::Value::F64(x)
        } else if let Ok(x) = v.extract::<bool>() {
            gguf_file::Value::Bool(x)
        } else if let Ok(x) = v.extract::<String>() {
            gguf_file::Value::String(x)
        } else if let Ok(x) = v.extract::<Vec<PyObject>>() {
            let x = x
                .into_iter()
                .map(|f| pyobject_to_gguf_value(f.as_ref(py), py))
                .collect::<PyResult<Vec<_>>>()?;
            gguf_file::Value::Array(x)
        } else {
            return Err(PyErr::new::<PyValueError, _>(format!(
                "unsupported type {:?}",
                v
            )));
        };
        Ok(v)
    }
    let tensors = tensors
        .extract::<&PyDict>(py)
        .map_err(|_| PyErr::new::<PyValueError, _>("expected a dict"))?
        .iter()
        .map(|(key, value)| {
            Ok((
                key.extract::<String>()
                    .map_err(|_| PyErr::new::<PyValueError, _>("keys must be strings"))?,
                value.extract::<PyQTensor>()?.0,
            ))
        })
        .collect::<PyResult<Vec<_>>>()?;

    let metadata = metadata
        .extract::<&PyDict>(py)
        .map_err(|_| PyErr::new::<PyValueError, _>("expected a dict"))?
        .iter()
        .map(|(key, value)| {
            Ok((
                key.extract::<String>()
                    .map_err(|_| PyErr::new::<PyValueError, _>("keys must be strings"))?,
                pyobject_to_gguf_value(value, py)?,
            ))
        })
        .collect::<PyResult<Vec<_>>>()?;

    let converted_metadata: Vec<_> = metadata
        .iter()
        .map(|(name, value)| (name.as_str(), value))
        .collect();

    let converted_tensors: Vec<_> = tensors
        .iter()
        .map(|(name, tensor)| (name.as_str(), tensor.as_ref()))
        .collect();

    let mut file = std::fs::File::create(path)?;

    gguf_file::write(&mut file, &converted_metadata, &converted_tensors).map_err(wrap_err)
}

#[pyfunction]
/// Returns true if the 'cuda' backend is available.
/// &RETURNS&: bool
fn cuda_is_available() -> bool {
    ::candle::utils::cuda_is_available()
}

#[pyfunction]
/// Returns true if candle was compiled with 'accelerate' support.
/// &RETURNS&: bool
fn has_accelerate() -> bool {
    ::candle::utils::has_accelerate()
}

#[pyfunction]
/// Returns true if candle was compiled with MKL support.
/// &RETURNS&: bool
fn has_mkl() -> bool {
    ::candle::utils::has_mkl()
}

#[pyfunction]
/// Returns the number of threads used by the candle.
/// &RETURNS&: int
fn get_num_threads() -> usize {
    ::candle::utils::get_num_threads()
}

fn candle_utils(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(cuda_is_available, m)?)?;
    m.add_function(wrap_pyfunction!(get_num_threads, m)?)?;
    m.add_function(wrap_pyfunction!(has_accelerate, m)?)?;
    m.add_function(wrap_pyfunction!(has_mkl, m)?)?;
    m.add_function(wrap_pyfunction!(load_ggml, m)?)?;
    m.add_function(wrap_pyfunction!(load_gguf, m)?)?;
    m.add_function(wrap_pyfunction!(save_gguf, m)?)?;
    m.add_function(wrap_pyfunction!(load_safetensors, m)?)?;
    m.add_function(wrap_pyfunction!(save_safetensors, m)?)?;
    Ok(())
}

#[pyfunction]
#[pyo3(text_signature = "(tensor:Tensor, dim:int)")]
/// Applies the Softmax function to a given tensor.#
/// &RETURNS&: Tensor
fn softmax(tensor: PyTensor, dim: i64) -> PyResult<PyTensor> {
    let dim = actual_dim(&tensor, dim).map_err(wrap_err)?;
    let sm = candle_nn::ops::softmax(&tensor.0, dim).map_err(wrap_err)?;
    Ok(PyTensor(sm))
}

#[pyfunction]
#[pyo3(text_signature = "(tensor:Tensor)")]
/// Applies the Sigmoid Linear Unit (SiLU) function to a given tensor.
/// &RETURNS&: Tensor
fn silu(tensor: PyTensor) -> PyResult<PyTensor> {
    let s = candle_nn::ops::silu(&tensor.0).map_err(wrap_err)?;
    Ok(PyTensor(s))
}

fn candle_nn_m(_py: Python<'_>, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(silu, m)?)?;
    m.add_function(wrap_pyfunction!(softmax, m)?)?;
    Ok(())
}

#[pymodule]
fn candle(py: Python<'_>, m: &PyModule) -> PyResult<()> {
    let utils = PyModule::new(py, "utils")?;
    candle_utils(py, utils)?;
    m.add_submodule(utils)?;
    let nn = PyModule::new(py, "nn")?;
    candle_nn_m(py, nn)?;
    m.add_submodule(nn)?;
    m.add_class::<PyTensor>()?;
    m.add_class::<PyQTensor>()?;
    m.add_class::<PyDType>()?;
    m.add("u8", PyDType(DType::U8))?;
    m.add("u32", PyDType(DType::U32))?;
    m.add("i16", PyDType(DType::I64))?;
    m.add("bf16", PyDType(DType::BF16))?;
    m.add("f16", PyDType(DType::F16))?;
    m.add("f32", PyDType(DType::F32))?;
    m.add("f64", PyDType(DType::F64))?;
    m.add_function(wrap_pyfunction!(cat, m)?)?;
    m.add_function(wrap_pyfunction!(ones, m)?)?;
    m.add_function(wrap_pyfunction!(rand, m)?)?;
    m.add_function(wrap_pyfunction!(randn, m)?)?;
    m.add_function(wrap_pyfunction!(tensor, m)?)?;
    m.add_function(wrap_pyfunction!(stack, m)?)?;
    m.add_function(wrap_pyfunction!(zeros, m)?)?;
    Ok(())
}
