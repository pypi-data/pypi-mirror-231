import os

from pydantic import BaseModel

from ssb_datahub.exceptions import EnvironmentException


class Environment(BaseModel):
    metadata_service_url: str
    data_service_url: str


def initialize_environment() -> Environment:
    try:
        return Environment(
            metadata_service_url=os.environ[
                "DATAHUB_CLIENT_METADATA_SERVICE_URL"
            ],
            data_service_url=os.environ["DATAHUB_CLIENT_DATA_SERVICE_URL"],
        )
    except Exception as e:
        raise EnvironmentException(
            "Exception occurred while initializing environment"
        ) from e


environment_variables = initialize_environment()
