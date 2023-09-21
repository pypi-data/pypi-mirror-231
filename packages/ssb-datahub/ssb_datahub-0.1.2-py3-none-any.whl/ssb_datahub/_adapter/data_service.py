from typing import Dict

import pyarrow
from pyarrow import parquet
import requests
from requests import Response

from ssb_datahub._config.environment import environment_variables
from ssb_datahub.exceptions import ServerException


DATA_SERVICE_URL = environment_variables.data_service_url


def _validate(response: Response):
    if response.status_code != 200:
        raise ServerException(response.text)


def get_fixed(query: Dict):
    response = requests.post(f"{DATA_SERVICE_URL}/fixed", json=query)
    _validate(response)
    reader = pyarrow.BufferReader(response.content)
    table = parquet.read_table(reader)
    return table


def get_status(query: Dict):
    response = requests.post(f"{DATA_SERVICE_URL}/status", json=query)
    _validate(response)
    reader = pyarrow.BufferReader(response.content)
    table = parquet.read_table(reader)
    return table


def get_accumulated(query: Dict):
    response = requests.post(f"{DATA_SERVICE_URL}/accumulated", json=query)
    _validate(response)
    reader = pyarrow.BufferReader(response.content)
    table = parquet.read_table(reader)
    return table


def get_event(query: Dict):
    response = requests.post(f"{DATA_SERVICE_URL}/event", json=query)
    _validate(response)
    reader = pyarrow.BufferReader(response.content)
    table = parquet.read_table(reader)
    return table
