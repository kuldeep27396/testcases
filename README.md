# TestCases — PySpark Data Processor (Tested)

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![PySpark](https://img.shields.io/badge/PySpark-3.5+-e25a1c)
![Tests](https://img.shields.io/badge/Tests-pytest%20%2B%20chispa-success)
![CI](https://img.shields.io/badge/CI-GitHub%20Actions-2088ff?logo=githubactions&logoColor=white)

> A **PySpark data-processor** library demonstrating test-driven data transformations — with a pytest + chispa test suite, GitHub Actions CI, and Codecov coverage tracking.

![Tests](https://github.com/kuldeep27396/testcases/actions/workflows/python-app.yml/badge.svg)
[![codecov](https://codecov.io/github/kuldeep27396/testcases/branch/main/graph/badge.svg)](https://codecov.io/gh/kuldeep27396/testcases)

## Overview

This project showcases building **reliable Spark data transformations** with proper testing. Instead of untested notebooks, it packages a data processor with a dedicated test suite using `chispa` for DataFrame equality assertions and `pytest-spark` for Spark session fixtures — wired into CI for every push.

## Features

- 🔧 **Reusable transformers** (`src/data_processor/transformer.py`)
- ⚙️ **Centralized Spark config** (`src/config/spark_config.py`)
- ✅ **Tested** with `pytest` + `chispa` (DataFrame equality) + `pytest-spark`
- 🤖 **CI** via GitHub Actions on every push
- 📊 **Coverage** tracked with Codecov

## Tech Stack

| Area | Technology |
|------|-----------|
| Processing | Apache Spark / PySpark 3.5+ |
| Testing | pytest, pytest-spark, chispa |
| Packaging | setuptools (`src` layout) |
| CI/CD | GitHub Actions + Codecov |

## Project Structure

```
├── main.py                         # Entry point
├── setup.py                        # Package definition (data-processor)
├── requirements.txt
├── src/
│   ├── config/
│   │   └── spark_config.py         # SparkSession configuration
│   ├── data_processor/
│   │   └── transformer.py          # Data transformation logic
│   └── tests/
│       └── test_transformer.py     # chispa-based DataFrame tests
└── .github/workflows/              # CI pipeline
```

## How to Run

```bash
# Install (editable) with the test extras
pip install -e . "pyspark>=3.5.0" pytest pytest-spark chispa

# Run the test suite
pytest

# Run the app
python main.py
```

## Author

**Kuldeep Pal** — [GitHub](https://github.com/kuldeep27396) · [Portfolio](https://www.kuldeep-pal.in/)
