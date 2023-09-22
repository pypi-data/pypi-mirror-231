mod parse_duration;
mod parse_rss;
use std::{mem, ops::Deref, sync::Arc, thread::JoinHandle};

use futures::lock::Mutex;
use parse_rss::PodcastFromRss;
use pyo3::{
    exceptions,
    prelude::*,
    types::{PyDict, PyList},
    wrap_pyfunction,
};

/// Formats the sum of two numbers as string.
#[pyfunction]
fn parse_single_podcast(
    py: Python<'_>,
    url: String,
    allow_exceptions: bool,
    request_timeout: u64,
) -> PyResult<&PyAny> {
    let url = Arc::new(url);

    pyo3_asyncio::tokio::future_into_py(py, async move {
        let url = Arc::clone(&url);

        let rss_text = parse_rss::fetch(&url.to_string(), &request_timeout).await;

        if rss_text.is_err() {
            if allow_exceptions {
                return Err(PyErr::new::<pyo3::exceptions::PyException, _>(format!(
                    "{:?}",
                    rss_text.err().unwrap()
                )));
            } else {
                return Ok(Python::with_gil(|py| py.None()));
            }
        }

        let rss_text = rss_text.unwrap();

        let parsed_podcast = parse_rss::parse(&rss_text);

        if parsed_podcast.is_err() {
            if allow_exceptions {
                return Err(PyErr::new::<pyo3::exceptions::PyException, _>(format!(
                    "{:?}",
                    parsed_podcast.err().unwrap()
                )));
            } else {
                return Ok(Python::with_gil(|py| py.None()));
            }
        }

        let parsed_podcast = parsed_podcast.unwrap();

        return Ok(Python::with_gil(|py| parsed_podcast.into_py(py)));
    })
}

#[pyfunction]
fn parse_list_of_podcasts(
    py: Python<'_>,
    urls: Vec<String>,
    verbose: bool,
    request_timeout: u64,
) -> PyResult<&PyAny> {
    pyo3_asyncio::tokio::future_into_py(py, async move {
        let urls = Arc::new(urls);

        let parsed_podcasts: Vec<Option<PodcastFromRss>> = vec![None; urls.len()];

        let parsed_podcasts = Arc::new(Mutex::new(parsed_podcasts));

        let mut tasks = Vec::with_capacity(urls.len());

        for i in 0..urls.len() {
            let urls = Arc::clone(&urls);
            let parsed_podcasts = Arc::clone(&parsed_podcasts);

            let task = tokio::spawn(async move {
                let url = Arc::clone(&urls);
                let parsed_podcasts = Arc::clone(&parsed_podcasts);

                let rss_text = parse_rss::fetch(&url[i].to_string(), &request_timeout).await;

                if rss_text.is_err() {
                    parsed_podcasts.lock().await[i] = None;
                    println!("{:?}", rss_text.err().unwrap());
                    return;
                }

                let rss_text = rss_text.unwrap();

                let parsed_podcast = parse_rss::parse(&rss_text);

                if parsed_podcast.is_err() {
                    parsed_podcasts.lock().await[i] = None;
                    println!("{:?}", parsed_podcast.err().unwrap());
                    return;
                }

                let parsed_podcast = parsed_podcast.unwrap();
                parsed_podcasts.lock().await[i] = Some(parsed_podcast);
            });

            tasks.push(task);
        }

        for task in tasks {
            let res = task.await;

            match res {
                Ok(_) => {}
                Err(e) => {
                    // print the error
                    if verbose {
                        println!("{:?}", e)
                    }
                }
            }
        }

        // unwrap the Arc and Mutex and get the inner value
        let completed_podcasts = Arc::try_unwrap(parsed_podcasts).unwrap();
        let completed_podcasts = completed_podcasts.into_inner();

        return Ok(Python::with_gil(|py| completed_podcasts.into_py(py)));
    })
}

/// A Python module implemented in Rust.
#[pymodule]
fn py_podcast_parser(_py: Python, m: &PyModule) -> PyResult<()> {
    m.add_function(wrap_pyfunction!(parse_single_podcast, m)?)?;
    m.add_function(wrap_pyfunction!(parse_list_of_podcasts, m)?)?;

    Ok(())
}
