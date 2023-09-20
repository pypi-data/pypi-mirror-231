use pyo3::{prelude::*};
use pyo3::class::basic::CompareOp;
use std::{sync::atomic::{AtomicUsize, Ordering}};

// Structs and methods to be used in python

#[pyclass]
pub struct Game {
    #[pyo3(get)]
    title: String,
    #[pyo3(get)]
    players: u8,
    #[pyo3(get)]
    gametype: Type,
}

//#[pyo3(get, set)]

impl Default for Game {
    fn default() -> Self {
        Game { title: "Game".to_string(), players: 2, gametype: Type::Normal}
    }
}

#[pymethods]
impl Game {
    #[new]
    fn new(title: String, players: u8, gametype: Type) -> Self {
        Game{ title, players, gametype }
    }
}

#[pyclass]
#[derive(Clone)]
pub enum Type {
    Normal,
    Extensive,
}

struct Utility {
    variable: Variable,
    numeral: i32,
}

// 

static VAR_ID: AtomicUsize = AtomicUsize::new(0);

#[pyclass]
#[derive(Clone)]
pub struct Variable {
    #[pyo3(get)]
    name: String,
    #[pyo3(get)]
    id: usize,
    #[pyo3(get)]
    lower: Vec<usize>,
    #[pyo3(get)]
    higher: Vec<usize>,
    #[pyo3(get)]
    equal: Vec<usize>,
    /*
    value: Value,
    id: u16,
    */
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
            CompareOp::Lt => self.higher.push(other.id),
            CompareOp::Eq => self.equal.push(other.id),
            CompareOp::Gt => self.lower.push(other.id),
            _ => (),
        }

        other.clone().into_py(py)
        // implement general function for adding to internal lists?
        // make variables a part of Game??
    }

}

//Because these types are references, in some situations 
//the Rust compiler may ask for lifetime annotations. If this is the case, you should use Py<PyAny>



struct Value {
    numeral: u16,
    variable: String,
}

struct Decision {
    player: Player,
    name: String,
    utility: Utility, 
    children: Box<Decision>,
}

struct Player {
    name: String,
}


pub fn add(a: i32, b: i32) -> i32 {
    a + b
}

#[cfg(test)]
mod tests {
    
    // importing names from outer scope.
    use super::*;

    #[test]
    fn test_add() {
        assert_eq!(add(1, 2), 3);
    }

}