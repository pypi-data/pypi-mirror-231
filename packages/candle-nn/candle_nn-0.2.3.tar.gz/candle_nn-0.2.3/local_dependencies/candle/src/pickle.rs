// Just enough pickle support to be able to read PyTorch checkpoints.
// This hardcodes objects that are required for tensor reading, we may want to make this a bit more
// composable/tensor agnostic at some point.
use crate::{DType, Error as E, Layout, Result, Tensor};
use byteorder::{LittleEndian, ReadBytesExt};
use std::collections::HashMap;
use std::io::BufRead;

const VERBOSE: bool = false;

// https://docs.juliahub.com/Pickle/LAUNc/0.1.0/opcode/
#[repr(u8)]
#[derive(Debug, Eq, PartialEq, Clone)]
pub enum OpCode {
    // https://github.com/python/cpython/blob/ed25f097160b5cbb0c9a1f9a746d2f1bbc96515a/Lib/pickletools.py#L2123
    Proto = 0x80,
    Global = b'c',
    BinPut = b'q',
    LongBinPut = b'r',
    EmptyTuple = b')',
    Reduce = b'R',
    Mark = b'(',
    BinUnicode = b'X',
    BinInt = b'J',
    Tuple = b't',
    BinPersId = b'Q',
    BinInt1 = b'K',
    BinInt2 = b'M',
    Tuple1 = 0x85,
    Tuple2 = 0x86,
    Tuple3 = 0x87,
    NewTrue = 0x88,
    NewFalse = 0x89,
    None = b'N',
    BinGet = b'h',
    LongBinGet = b'j',
    SetItem = b's',
    SetItems = b'u',
    EmptyDict = b'}',
    Dict = b'd',
    Build = b'b',
    Stop = b'.',
    NewObj = 0x81,
    EmptyList = b']',
    BinFloat = b'g',
    Append = b'a',
    Appends = b'e',
}

// Avoid using FromPrimitive so as not to drag another dependency.
impl TryFrom<u8> for OpCode {
    type Error = u8;
    fn try_from(value: u8) -> std::result::Result<Self, Self::Error> {
        match value {
            0x80 => Ok(Self::Proto),
            b'c' => Ok(Self::Global),
            b'q' => Ok(Self::BinPut),
            b'r' => Ok(Self::LongBinPut),
            b')' => Ok(Self::EmptyTuple),
            b'R' => Ok(Self::Reduce),
            b'(' => Ok(Self::Mark),
            b'X' => Ok(Self::BinUnicode),
            b'J' => Ok(Self::BinInt),
            b't' => Ok(Self::Tuple),
            b'Q' => Ok(Self::BinPersId),
            b'K' => Ok(Self::BinInt1),
            b'M' => Ok(Self::BinInt2),
            b'N' => Ok(Self::None),
            0x85 => Ok(Self::Tuple1),
            0x86 => Ok(Self::Tuple2),
            0x87 => Ok(Self::Tuple3),
            0x88 => Ok(Self::NewTrue),
            0x89 => Ok(Self::NewFalse),
            b'h' => Ok(Self::BinGet),
            b'j' => Ok(Self::LongBinGet),
            b's' => Ok(Self::SetItem),
            b'u' => Ok(Self::SetItems),
            b'}' => Ok(Self::EmptyDict),
            b'd' => Ok(Self::EmptyDict),
            b'b' => Ok(Self::Build),
            b'.' => Ok(Self::Stop),
            0x81 => Ok(Self::NewObj),
            b']' => Ok(Self::EmptyList),
            b'G' => Ok(Self::BinFloat),
            b'a' => Ok(Self::Append),
            b'e' => Ok(Self::Appends),
            value => Err(value),
        }
    }
}

fn read_to_newline<R: BufRead>(r: &mut R) -> Result<Vec<u8>> {
    let mut data: Vec<u8> = Vec::with_capacity(32);
    r.read_until(b'\n', &mut data)?;
    data.pop();
    if data.last() == Some(&b'\r') {
        data.pop();
    }
    Ok(data)
}

#[derive(Debug, Clone, PartialEq)]
pub enum Object {
    Class {
        module_name: String,
        class_name: String,
    },
    Int(i32),
    Float(f64),
    Unicode(String),
    Bool(bool),
    None,
    Tuple(Vec<Object>),
    List(Vec<Object>),
    Mark,
    Dict(Vec<(Object, Object)>),
    Reduce {
        callable: Box<Object>,
        args: Box<Object>,
    },
    Build {
        callable: Box<Object>,
        args: Box<Object>,
    },
    PersistentLoad(Box<Object>),
}

type OResult<T> = std::result::Result<T, Object>;

impl Object {
    pub fn unicode(self) -> OResult<String> {
        match self {
            Self::Unicode(t) => Ok(t),
            _ => Err(self),
        }
    }

    pub fn reduce(self) -> OResult<(Self, Self)> {
        match self {
            Self::Reduce { callable, args } => Ok((*callable, *args)),
            _ => Err(self),
        }
    }

    pub fn none(self) -> OResult<()> {
        match self {
            Self::None => Ok(()),
            _ => Err(self),
        }
    }

    pub fn persistent_load(self) -> OResult<Self> {
        match self {
            Self::PersistentLoad(t) => Ok(*t),
            _ => Err(self),
        }
    }

    pub fn bool(self) -> OResult<bool> {
        match self {
            Self::Bool(t) => Ok(t),
            _ => Err(self),
        }
    }

    pub fn int(self) -> OResult<i32> {
        match self {
            Self::Int(t) => Ok(t),
            _ => Err(self),
        }
    }

    pub fn tuple(self) -> OResult<Vec<Self>> {
        match self {
            Self::Tuple(t) => Ok(t),
            _ => Err(self),
        }
    }

    pub fn dict(self) -> OResult<Vec<(Self, Self)>> {
        match self {
            Self::Dict(t) => Ok(t),
            _ => Err(self),
        }
    }

    pub fn class(self) -> OResult<(String, String)> {
        match self {
            Self::Class {
                module_name,
                class_name,
            } => Ok((module_name, class_name)),
            _ => Err(self),
        }
    }
}

impl TryFrom<Object> for String {
    type Error = Object;
    fn try_from(value: Object) -> std::result::Result<Self, Self::Error> {
        match value {
            Object::Unicode(s) => Ok(s),
            other => Err(other),
        }
    }
}

impl TryFrom<Object> for usize {
    type Error = Object;
    fn try_from(value: Object) -> std::result::Result<Self, Self::Error> {
        match value {
            Object::Int(s) if s >= 0 => Ok(s as usize),
            other => Err(other),
        }
    }
}

impl<T: TryFrom<Object, Error = Object>> TryFrom<Object> for Vec<T> {
    type Error = Object;
    fn try_from(value: Object) -> std::result::Result<Self, Self::Error> {
        match value {
            Object::Tuple(values) => {
                // This does not return the appropriate value in the error case but instead return
                // the object related to the first error.
                values
                    .into_iter()
                    .map(|v| T::try_from(v))
                    .collect::<std::result::Result<Vec<T>, Self::Error>>()
            }
            other => Err(other),
        }
    }
}

#[derive(Debug)]
pub struct Stack {
    stack: Vec<Object>,
    memo: HashMap<u32, Object>,
}

impl Stack {
    pub fn empty() -> Self {
        Self {
            stack: Vec::with_capacity(512),
            memo: HashMap::new(),
        }
    }

    pub fn stack(&self) -> &[Object] {
        self.stack.as_slice()
    }

    pub fn read_loop<R: BufRead>(&mut self, r: &mut R) -> Result<()> {
        loop {
            if self.read(r)? {
                break;
            }
        }
        Ok(())
    }

    pub fn finalize(mut self) -> Result<Object> {
        self.pop()
    }

    fn push(&mut self, obj: Object) {
        self.stack.push(obj)
    }

    fn pop(&mut self) -> Result<Object> {
        match self.stack.pop() {
            None => crate::bail!("unexpected empty stack"),
            Some(obj) => Ok(obj),
        }
    }

    // https://docs.juliahub.com/Pickle/LAUNc/0.1.0/opcode/#Pickle.OpCodes.BUILD
    fn build(&mut self) -> Result<()> {
        let args = self.pop()?;
        let obj = self.pop()?;
        let obj = match (obj, args) {
            (Object::Dict(mut obj), Object::Dict(mut args)) => {
                obj.append(&mut args);
                Object::Dict(obj)
            }
            (obj, args) => Object::Build {
                callable: Box::new(obj),
                args: Box::new(args),
            },
        };
        self.push(obj);
        Ok(())
    }

    fn reduce(&mut self) -> Result<()> {
        let args = self.pop()?;
        let callable = self.pop()?;
        #[allow(clippy::single_match)]
        let reduced = match &callable {
            Object::Class {
                module_name,
                class_name,
            } => {
                if module_name == "collections" && class_name == "OrderedDict" {
                    // TODO: have a separate ordered dict.
                    Some(Object::Dict(vec![]))
                } else {
                    None
                }
            }
            _ => None,
        };
        let reduced = reduced.unwrap_or_else(|| Object::Reduce {
            callable: Box::new(callable),
            args: Box::new(args),
        });
        self.push(reduced);
        Ok(())
    }

    fn last(&mut self) -> Result<&mut Object> {
        match self.stack.last_mut() {
            None => crate::bail!("unexpected empty stack"),
            Some(obj) => Ok(obj),
        }
    }

    fn memo_get(&self, id: u32) -> Result<Object> {
        match self.memo.get(&id) {
            None => crate::bail!("missing object in memo {id}"),
            Some(obj) => {
                // Maybe we should use refcounting rather than doing potential large clones here.
                Ok(obj.clone())
            }
        }
    }

    fn memo_put(&mut self, id: u32) -> Result<()> {
        let obj = self.last()?.clone();
        self.memo.insert(id, obj);
        Ok(())
    }

    fn persistent_load(&self, id: Object) -> Result<Object> {
        Ok(Object::PersistentLoad(Box::new(id)))
    }

    fn new_obj(&self, class: Object, args: Object) -> Result<Object> {
        Ok(Object::Reduce {
            callable: Box::new(class),
            args: Box::new(args),
        })
    }

    fn pop_to_marker(&mut self) -> Result<Vec<Object>> {
        let mut mark_idx = None;
        for (idx, obj) in self.stack.iter().enumerate().rev() {
            if obj == &Object::Mark {
                mark_idx = Some(idx);
                break;
            }
        }
        match mark_idx {
            Some(mark_idx) => {
                let objs = self.stack.split_off(mark_idx + 1);
                self.stack.pop();
                Ok(objs)
            }
            None => {
                crate::bail!("marker object not found")
            }
        }
    }

    pub fn read<R: BufRead>(&mut self, r: &mut R) -> Result<bool> {
        let op_code = match OpCode::try_from(r.read_u8()?) {
            Ok(op_code) => op_code,
            Err(op_code) => {
                crate::bail!("unknown op-code {op_code}")
            }
        };
        // println!("op: {op_code:?}");
        // println!("{:?}", self.stack);
        match op_code {
            OpCode::Proto => {
                let version = r.read_u8()?;
                if VERBOSE {
                    println!("proto {version}");
                }
            }
            OpCode::Global => {
                let module_name = read_to_newline(r)?;
                let class_name = read_to_newline(r)?;
                let module_name = String::from_utf8_lossy(&module_name).to_string();
                let class_name = String::from_utf8_lossy(&class_name).to_string();
                self.push(Object::Class {
                    module_name,
                    class_name,
                })
            }
            OpCode::BinInt1 => {
                let arg = r.read_u8()?;
                self.push(Object::Int(arg as i32))
            }
            OpCode::BinInt2 => {
                let arg = r.read_u16::<LittleEndian>()?;
                self.push(Object::Int(arg as i32))
            }
            OpCode::BinInt => {
                let arg = r.read_i32::<LittleEndian>()?;
                self.push(Object::Int(arg))
            }
            OpCode::BinFloat => {
                let arg = r.read_f64::<LittleEndian>()?;
                self.push(Object::Float(arg))
            }
            OpCode::BinUnicode => {
                let len = r.read_u32::<LittleEndian>()?;
                let mut data = vec![0u8; len as usize];
                r.read_exact(&mut data)?;
                let data = String::from_utf8(data).map_err(E::wrap)?;
                self.push(Object::Unicode(data))
            }
            OpCode::BinPersId => {
                let id = self.pop()?;
                let obj = self.persistent_load(id)?;
                self.push(obj)
            }
            OpCode::Tuple => {
                let objs = self.pop_to_marker()?;
                self.push(Object::Tuple(objs))
            }
            OpCode::Tuple1 => {
                let obj = self.pop()?;
                self.push(Object::Tuple(vec![obj]))
            }
            OpCode::Tuple2 => {
                let obj2 = self.pop()?;
                let obj1 = self.pop()?;
                self.push(Object::Tuple(vec![obj1, obj2]))
            }
            OpCode::Tuple3 => {
                let obj3 = self.pop()?;
                let obj2 = self.pop()?;
                let obj1 = self.pop()?;
                self.push(Object::Tuple(vec![obj1, obj2, obj3]))
            }
            OpCode::NewTrue => self.push(Object::Bool(true)),
            OpCode::NewFalse => self.push(Object::Bool(false)),
            OpCode::Append => {
                let value = self.pop()?;
                let pylist = self.last()?;
                if let Object::List(d) = pylist {
                    d.push(value)
                } else {
                    crate::bail!("expected a list, got {pylist:?}")
                }
            }
            OpCode::Appends => {
                let objs = self.pop_to_marker()?;
                let pylist = self.last()?;
                if let Object::List(d) = pylist {
                    d.extend(objs)
                } else {
                    crate::bail!("expected a list, got {pylist:?}")
                }
            }
            OpCode::SetItem => {
                let value = self.pop()?;
                let key = self.pop()?;
                let pydict = self.last()?;
                if let Object::Dict(d) = pydict {
                    d.push((key, value))
                } else {
                    crate::bail!("expected a dict, got {pydict:?}")
                }
            }
            OpCode::SetItems => {
                let mut objs = self.pop_to_marker()?;
                let pydict = self.last()?;
                if let Object::Dict(d) = pydict {
                    if objs.len() % 2 != 0 {
                        crate::bail!("setitems: not an even number of objects")
                    }
                    while let Some(value) = objs.pop() {
                        let key = objs.pop().unwrap();
                        d.push((key, value))
                    }
                } else {
                    crate::bail!("expected a dict, got {pydict:?}")
                }
            }
            OpCode::None => self.push(Object::None),
            OpCode::Stop => {
                return Ok(true);
            }
            OpCode::Build => self.build()?,
            OpCode::EmptyDict => self.push(Object::Dict(vec![])),
            OpCode::Dict => {
                let mut objs = self.pop_to_marker()?;
                let mut pydict = vec![];
                if objs.len() % 2 != 0 {
                    crate::bail!("setitems: not an even number of objects")
                }
                while let Some(value) = objs.pop() {
                    let key = objs.pop().unwrap();
                    pydict.push((key, value))
                }
                self.push(Object::Dict(pydict))
            }
            OpCode::Mark => self.push(Object::Mark),
            OpCode::Reduce => self.reduce()?,
            OpCode::EmptyTuple => self.push(Object::Tuple(vec![])),
            OpCode::EmptyList => self.push(Object::List(vec![])),
            OpCode::BinGet => {
                let arg = r.read_u8()?;
                let obj = self.memo_get(arg as u32)?;
                self.push(obj)
            }
            OpCode::LongBinGet => {
                let arg = r.read_u32::<LittleEndian>()?;
                let obj = self.memo_get(arg)?;
                self.push(obj)
            }
            OpCode::BinPut => {
                let arg = r.read_u8()?;
                self.memo_put(arg as u32)?
            }
            OpCode::LongBinPut => {
                let arg = r.read_u32::<LittleEndian>()?;
                self.memo_put(arg)?
            }
            OpCode::NewObj => {
                let args = self.pop()?;
                let class = self.pop()?;
                let obj = self.new_obj(class, args)?;
                self.push(obj)
            }
        }
        Ok(false)
    }
}

impl From<Object> for E {
    fn from(value: Object) -> Self {
        E::Msg(format!("conversion error on {value:?}"))
    }
}

// https://github.com/pytorch/pytorch/blob/4eac43d046ded0f0a5a5fa8db03eb40f45bf656e/torch/_utils.py#L198
// Arguments: storage, storage_offset, size, stride, requires_grad, backward_hooks
fn rebuild_args(args: Object) -> Result<(Layout, DType, String, usize)> {
    let mut args = args.tuple()?;
    let stride = Vec::<usize>::try_from(args.remove(3))?;
    let size = Vec::<usize>::try_from(args.remove(2))?;
    let offset = args.remove(1).int()? as usize;
    let storage = args.remove(0).persistent_load()?;
    let mut storage = storage.tuple()?;
    let storage_size = storage.remove(4).int()? as usize;
    let path = storage.remove(2).unicode()?;
    let (_module_name, class_name) = storage.remove(1).class()?;
    let dtype = match class_name.as_str() {
        "FloatStorage" => DType::F32,
        "DoubleStorage" => DType::F64,
        "HalfStorage" => DType::F16,
        "BFloat16Storage" => DType::BF16,
        "ByteStorage" => DType::U8,
        other => {
            crate::bail!("unsupported storage type {other}")
        }
    };
    let layout = Layout::new(crate::Shape::from(size), stride, offset);
    Ok((layout, dtype, path, storage_size))
}

#[derive(Debug, Clone)]
pub struct TensorInfo {
    pub name: String,
    pub dtype: DType,
    pub layout: Layout,
    pub path: String,
    pub storage_size: usize,
}

pub fn read_pth_tensor_info<P: AsRef<std::path::Path>>(
    file: P,
    verbose: bool,
) -> Result<Vec<TensorInfo>> {
    let file = std::fs::File::open(file)?;
    let zip_reader = std::io::BufReader::new(file);
    let mut zip = zip::ZipArchive::new(zip_reader)?;
    let zip_file_names = zip
        .file_names()
        .map(|f| f.to_string())
        .collect::<Vec<String>>();

    let mut tensor_infos = vec![];
    for file_name in zip_file_names.iter() {
        if !file_name.ends_with("data.pkl") {
            continue;
        }
        let dir_name = std::path::PathBuf::from(file_name.strip_suffix(".pkl").unwrap());
        let reader = zip.by_name(file_name)?;
        let mut reader = std::io::BufReader::new(reader);
        let mut stack = Stack::empty();
        stack.read_loop(&mut reader)?;
        let obj = stack.finalize()?;
        if VERBOSE || verbose {
            println!("{obj:?}");
        }
        let obj = match obj {
            Object::Build { callable, args } => match *callable {
                Object::Reduce { callable, args: _ } => match *callable {
                    Object::Class {
                        module_name,
                        class_name,
                    } if module_name == "__torch__" && class_name == "Module" => *args,
                    _ => continue,
                },
                _ => continue,
            },
            obj => obj,
        };
        if let Object::Dict(key_values) = obj {
            for (name, value) in key_values.into_iter() {
                let name = match name.unicode() {
                    Ok(name) => name,
                    Err(_) => continue,
                };
                let (callable, args) = match value.reduce() {
                    Ok(callable_args) => callable_args,
                    _ => continue,
                };
                let (callable, args) = match callable {
                    Object::Class {
                        module_name,
                        class_name,
                    } if module_name == "torch._tensor"
                        && class_name == "_rebuild_from_type_v2" =>
                    {
                        let mut args = args.tuple()?;
                        let callable = args.remove(0);
                        let args = args.remove(1);
                        (callable, args)
                    }
                    _ => (callable, args),
                };
                match callable {
                    Object::Class {
                        module_name,
                        class_name,
                    } if module_name == "torch._utils" && class_name == "_rebuild_tensor_v2" => {}
                    _ => continue,
                };
                match rebuild_args(args) {
                    Ok((layout, dtype, file_path, storage_size)) => {
                        let mut path = dir_name.clone();
                        path.push(file_path);
                        tensor_infos.push(TensorInfo {
                            name,
                            dtype,
                            layout,
                            path: path.to_string_lossy().into_owned(),
                            storage_size,
                        })
                    }
                    Err(err) => {
                        eprintln!("skipping {name}: {err:?}")
                    }
                }
            }
        }
    }
    Ok(tensor_infos)
}

/// Lazy tensor loader.
pub struct PthTensors {
    tensor_infos: HashMap<String, TensorInfo>,
    path: std::path::PathBuf,
    // We do not store a zip reader as it needs mutable access to extract data. Instead we
    // re-create a zip reader for each tensor.
}

impl PthTensors {
    pub fn new<P: AsRef<std::path::Path>>(path: P) -> Result<Self> {
        let tensor_infos = read_pth_tensor_info(path.as_ref(), false)?;
        let tensor_infos = tensor_infos
            .into_iter()
            .map(|ti| (ti.name.to_string(), ti))
            .collect();
        let path = path.as_ref().to_owned();
        Ok(Self { tensor_infos, path })
    }

    pub fn tensor_infos(&self) -> &HashMap<String, TensorInfo> {
        &self.tensor_infos
    }

    pub fn get(&self, name: &str) -> Result<Option<Tensor>> {
        let tensor_info = match self.tensor_infos.get(name) {
            None => return Ok(None),
            Some(tensor_info) => tensor_info,
        };
        // We hope that the file has not changed since first reading it.
        let zip_reader = std::io::BufReader::new(std::fs::File::open(&self.path)?);
        let mut zip = zip::ZipArchive::new(zip_reader)?;
        let mut reader = zip.by_name(&tensor_info.path)?;

        // Reading the data is a bit tricky as it can be strided, use an offset, etc.
        // For now only support the basic case.
        if tensor_info.layout.start_offset() != 0 || !tensor_info.layout.is_contiguous() {
            crate::bail!(
                "cannot retrieve non-contiguous tensors {:?}",
                tensor_info.layout
            )
        }
        let tensor = Tensor::from_reader(
            tensor_info.layout.shape().clone(),
            tensor_info.dtype,
            &mut reader,
        )?;
        Ok(Some(tensor))
    }
}
