use pyo3::{prelude::*};
use crate::node::*;

#[pyclass]
#[derive(Clone)]
pub struct Game {
    #[pyo3(get)]
    title: String,
    #[pyo3(get)]
    players: Vec<Player>,
    #[pyo3(get)]
    gametype: Type,
    #[pyo3(get)]
    root: Option<Decision>,
}

//#[pyo3(get, set)]

#[pymethods]
impl Game {
    #[new]
    fn new(title: Option<String>, gametype: Option<Type>) -> Self {
        Game{
            // TODO: make function that automakes players
            title: title.unwrap_or("Untitled Game".parse().unwrap()),
            players: Vec::new(),
            gametype: gametype.unwrap_or(Type::Normal),
            root: None
        }
    }
    fn add_root(&mut self, root: Decision){
        self.root = Option::from(root);
    }
    fn __add__(&mut self, other: &Decision, py: Python) -> Py<PyAny> {

        self.root = Option::from(other.clone());
        self.clone().into_py(py)

    }

}

#[pyclass]
#[derive(Clone)]
pub enum Type {
    Normal,
    Extensive,
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