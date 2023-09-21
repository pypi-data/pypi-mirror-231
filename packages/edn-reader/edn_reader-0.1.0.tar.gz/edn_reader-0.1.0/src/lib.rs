use std::collections::{BTreeMap, BTreeSet};
use std::io::BufRead;

use anyhow::anyhow;
use chrono::prelude::*;
use edn_rs::Edn;
use pyo3::prelude::*;
use pyo3::types::PyList;

struct MyEdn(Edn);

fn parse_rational(r: String) -> f64 {
    let parts = r.split("/").collect::<Vec<&str>>();
    let numerator = parts[0].parse::<f64>().unwrap_or(0.0f64);
    let denominator = parts[1].parse::<f64>().unwrap_or(1.0f64);
    numerator / denominator
}
impl IntoPy<PyObject> for MyEdn {
    fn into_py(self, py: Python<'_>) -> PyObject {
        match self.0 {
            Edn::Str(s) => s.into_py(py),
            Edn::Key(k) => k.into_py(py),
            Edn::Symbol(s) => s.into_py(py),
            Edn::Int(i) => i.into_py(py),
            Edn::UInt(i) => i.into_py(py),
            Edn::Double(d) => d.to_string().parse::<f64>().unwrap_or(0.0f64).into_py(py), // edn::Double is silly... :(
            Edn::Rational(r) => parse_rational(r).into_py(py),
            Edn::Bool(b) => b.into_py(py),
            Edn::Nil | Edn::Empty => None::<String>.into_py(py), // Use a type parameter to make the compiler happy
            Edn::Vector(v) => v
                .to_vec()
                .into_iter()
                .map(|x| MyEdn(x).into_py(py))
                .collect::<Vec<PyObject>>()
                .into_py(py),
            Edn::Map(m) => m
                .to_map()
                .into_iter()
                .map(|(k, v)| (k, MyEdn(v).into_py(py)))
                .collect::<BTreeMap<String, PyObject>>()
                .into_py(py),
            Edn::Set(_s) => todo!(), // s.to_set().into_iter().map(|x| MyEdn(x).into_py(py)).collect::<BTreeSet<PyObject>>().into_py(py),
            Edn::List(l) => l
                .to_vec()
                .into_iter()
                .map(|x| MyEdn(x).into_py(py))
                .collect::<Vec<PyObject>>()
                .into_py(py),
            Edn::Tagged(_t, _value) => todo!(),
            Edn::Char(c) => c.into_py(py),
            Edn::Uuid(_u) => todo!(),
            Edn::Inst(i) => i.parse::<DateTime<Utc>>().unwrap_or(Utc::now()).into_py(py),
            Edn::NamespacedMap(namespace, m) => m
                .to_map()
                .into_iter()
                .map(|(k, v)| (format!("{}/{}", namespace, k), MyEdn(v).into_py(py)))
                .collect::<BTreeMap<String, PyObject>>()
                .into_py(py),
        }
    }
}

#[pyfunction]
fn read_string(input: &str) -> PyResult<Py<PyAny>> {
    Python::with_gil(|py| -> PyResult<Py<PyAny>> {
        let edn = input
            .parse::<Edn>()
            .map_err(|e| anyhow!("Couldn't parse EDN.\n{e}"))?;
        let py_obj = MyEdn(edn).into_py(py);

        PyResult::Ok(py_obj)
    })
}

#[pyfunction]
fn read_file(filename: &str) -> PyResult<Py<PyList>> {
    let file = std::fs::File::open(filename)?;
    let reader = std::io::BufReader::new(file);
    let mut lines = Vec::new();
    for line in reader.lines() {
        let line = line?;
        let edn = line
            .parse::<Edn>()
            .map_err(|e| anyhow!("Couldn't parse EDN.\n{e}"))?;
        lines.push(edn);
    }
    Python::with_gil(|py| -> PyResult<Py<PyList>> {
        let list = PyList::empty(py);
        for line in lines {
            list.append(MyEdn(line).into_py(py))?;
        }
        PyResult::Ok(list.into())
    })
}

/// A Python module implemented in Rust.
#[pymodule]
fn edn_reader(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(read_string, m)?)?;
    m.add_function(wrap_pyfunction!(read_file, m)?)?;
    PyResult::Ok(())
}
