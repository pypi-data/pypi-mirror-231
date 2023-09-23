use pyo3::prelude::*;
use crate::game::*;
use crate::node::{Decision, Player};
use crate::utility::*;

mod game;
mod node;
mod utility;

/// Formats the sum of two numbers as string.
#[pyfunction]
fn sum_as_string(a: usize, b: usize) -> PyResult<String> {
    Ok((a + b).to_string())
}

/// A Python module implemented in Rust.
#[pymodule]
fn stratpy(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_class::<Game>()?;
    m.add_class::<Type>()?;
    m.add_class::<Variable>()?;
    m.add_class::<Decision>()?;
    m.add_class::<Player>()?;
    m.add_function(wrap_pyfunction!(sum_as_string, m)?)?;
    Ok(())
}

#[cfg(test)]
mod tests {
    use super::*;
  
    #[test]
    fn simple_test() {
        assert_eq!(sum_as_string(2,2).unwrap(), "4");
    }
}