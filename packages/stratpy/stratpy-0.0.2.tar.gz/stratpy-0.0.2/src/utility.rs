use pyo3::{prelude::*};
use pyo3::class::basic::CompareOp;
use std::{sync::atomic::{AtomicUsize, Ordering}};

struct Utility {
    variable: Variable,
    numeral: i32,
}

// atomic usize for ids
static VAR_ID: AtomicUsize = AtomicUsize::new(0);


// Make utility seperate from variable struct?

#[pyclass]
#[derive(Clone)]
pub struct Variable { // don't need getters in release
    #[pyo3(get)] name: String,
    #[pyo3(get)] id: usize,
    #[pyo3(get)] lower: Vec<usize>,
    #[pyo3(get)] higher: Vec<usize>,
    #[pyo3(get)] equal: Vec<usize>,
}

#[pymethods]
impl Variable {
    #[new]
    pub fn new(name: String) -> Self {
        Variable{
            name,
            id: VAR_ID.fetch_add(1, Ordering::SeqCst),
            lower: Vec::new(),
            higher: Vec::new(),
            equal: Vec::new()
        }
    }

    fn __richcmp__(&mut self, other: &Self, op: CompareOp, py: Python) -> PyObject {
        match op {
            // TODO: check for duplicates before pushing
            // TODO: add transitive feature if a > b and b > or == c then a > c!
            CompareOp::Lt => self.higher.push(other.id),
            CompareOp::Eq => self.equal.push(other.id),
            CompareOp::Gt => self.lower.push(other.id),
            _ => (),
        }

        other.clone().into_py(py)

    }

}

//Because these types are references, in some situations
//the Rust compiler may ask for lifetime annotations. If this is the case, you should use Py<PyAny>