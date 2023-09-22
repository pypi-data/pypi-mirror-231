import requests
from requests import Response

from ssb_datahub._config.environment import environment_variables
from ssb_datahub.exceptions import ServerException


METADATA_SERVICE_URL = environment_variables.metadata_service_url


def _validate(response: Response):
    if response.status_code != 200:
        raise ServerException(response.text)


def get_domain(domain_name: str):
    response = requests.get(f"{METADATA_SERVICE_URL}/domains/{domain_name}")
    _validate(response)
    return response.json()


def get_domains():
    response = requests.get(f"{METADATA_SERVICE_URL}/domains")
    _validate(response)
    return response.json()


def get_products_for_domain(domain_name: str):
    response = requests.get(f"{METADATA_SERVICE_URL}/domains/{domain_name}/products")
    _validate(response)
    return response.json()


def get_identifier(domain: str, name: str, version: str):
    response = requests.get(
        f"{METADATA_SERVICE_URL}/domains/{domain}/identifiers/{name}?version={version}"
    )
    _validate(response)
    return response.json()


def get_unit_type(domain: str, name: str, version: str):
    response = requests.get(
        f"{METADATA_SERVICE_URL}/domains/{domain}/unit-types/{name}?version={version}"
    )
    _validate(response)
    return response.json()


def get_codelist(domain: str, name: str, version: str):
    response = requests.get(
        f"{METADATA_SERVICE_URL}/domains/{domain}/codelists/{name}?version={version}"
    )
    _validate(response)
    return response.json()


def get_variable(domain: str, name: str, version: str):
    response = requests.get(
        f"{METADATA_SERVICE_URL}/domains/{domain}/variables/{name}?version={version}"
    )
    _validate(response)
    return response.json()
