<br />
<div align="center">
  <img src="images/logo.png" alt="Logo" width="80" height="80">
  <br />
  <h2 align="center">DATAHUB PYTHON CLIENT</h2>
  <br />
  <p align="center">

[![Poetry](https://img.shields.io/endpoint?url=https://python-poetry.org/badge/v0.json)](https://python-poetry.org/)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)][black]
[![PyPI](https://img.shields.io/pypi/v/ssb-datahub.svg)][pypi status]
[![Python Version](https://img.shields.io/pypi/pyversions/ssb-datahub)][pypi status]
[![License](https://img.shields.io/pypi/l/ssb-datahub)][license]
  </p>
  <p align="center">
    Client library for DataHub, a data platform developed at Statistics Norway
  </p>
  <br />
</div>

[license]: https://github.com/statisticsnorway/ssb-datahub/blob/main/LICENSE
[pypi status]: https://pypi.org/project/ssb-datahub/
[black]: https://github.com/psf/black

## Getting started

### Prerequisites

* [Install poetry](https://python-poetry.org/)

### Development environment

* Clone the repository
* Install the poetry environment

  ```sh
    poetry install
  ```

## Usage

```sh
pip install ssb-datahub
```

```python
from ssb_datahub import Client
dh = Client()

# Collect variables
kjonn = dh.get_variable("FREG", "BEFOLKNING_KJONN", "1.0.0")
fornavn = dh.get_variable("FREG", "BEFOLKNING_FORNAVN", "1.0.0")
fodt_aar = dh.get_variable("FREG", "BEFOLKNING_FODT_AAR", "1.0.0")

# Get the most popular names of men born in 1993
navnestatistikken_menn = (
    kjonn
        .left_join(fornavn, "IDENTIFIER")
        .filter("BEFOLKNING_KJONN", "1")
        .left_join(fodt_aar, "IDENTIFIER")
        .filter("BEFOLKNING_FODT_AAR", 1993)
        .count_values("BEFOLKNING_FORNAVN")
        .sort("BEFOLKNING_FORNAVN")
)
navnestatistikken_menn.sources
```
