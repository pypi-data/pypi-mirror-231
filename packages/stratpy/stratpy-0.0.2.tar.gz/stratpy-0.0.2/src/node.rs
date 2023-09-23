use pyo3::{prelude::*};

#[pyclass]
#[derive(Clone)]
pub struct Decision {
    #[pyo3(get)] player: Player, // make nature own struct?
    #[pyo3(get)] name: String,
    children: Vec<Box<Decision>>,
}

#[pymethods]
impl Decision {
    #[new]
    pub fn new(player: Player, name: String) -> Self {
        Decision{
            player,
            name,
            children: Vec::new(),
        }
    }
    pub fn add_child(&mut self, player: Player, name: String){
        self.children.push(Box::new(Decision::new(player, name)));
    }
}

#[pyclass]
#[derive(Clone)]
pub struct Player {
    #[pyo3(get)] name: String,
}


#[pymethods]
impl Player {
    #[new]
    pub fn new(name: String) -> Self {
        Player{ name, }
    }
}