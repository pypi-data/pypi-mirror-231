from typing import Dict, List, Optional, Union

import pyarrow
from pyarrow import compute
from pydantic import BaseModel

from ssb_datahub._adapter import metadata_service, data_service
from ssb_datahub.exceptions import DataQueryException


class ProductReference(BaseModel):
    domain: str
    name: str
    version: str


class Column:
    name: str
    unit_type: Optional[Union[ProductReference, None]] = None
    code_list: Optional[Union[ProductReference, None]] = None
    source: Optional[Union[ProductReference, None]] = None

    def __init__(
        self: "Column",
        name: str,
        unit_type: Optional[ProductReference] = None,
        code_list: Optional[ProductReference] = None,
        source: Optional[Union[ProductReference, None]] = None,
    ):
        self.name = name
        self.unit_type = unit_type
        self.code_list = code_list
        self.source = source


class Dataset:
    table: pyarrow.Table
    columns: List[Column]
    sources: List[ProductReference] = []

    def __init__(
        self: "Dataset",
        table: pyarrow.Table,
        columns: List[Column],
        sources: List[ProductReference] = [],
    ):
        self.table = table.rename_columns([column.name for column in columns])
        self.columns = columns
        self.sources = sources

    def filter(
        self: "Dataset",
        column_name: str,
        filter_in: Union[str, int, float, bool],
    ) -> "Dataset":
        filtered_table = self.table.filter(
            compute.field(column_name) == (filter_in)
        )
        return Dataset(
            table=filtered_table, columns=self.columns, sources=self.sources
        )

    def left_join(self: "Dataset", other: "Dataset", key: str) -> "Dataset":
        joined_table = self.table.join(other.table, key)
        return Dataset(
            table=joined_table,
            columns=(
                self.columns
                + [column for column in other.columns if column.name != key]
            ),
            sources=self.sources + other.sources,
        )

    def count_values(self: "Dataset", column_name: str) -> "Dataset":
        counted_table = self.table.group_by(column_name).aggregate(
            [(column_name, "count")]
        )
        return Dataset(
            table=counted_table,
            columns=[
                column for column in self.columns if column.name == column_name
            ]
            + [Column(name=f"{column_name}_COUNT")],
            sources=self.sources,
        )

    def sort(self: "Dataset", by_column: str) -> "Dataset":
        sorted_table = self.table.sort_by([(by_column, "descending")])
        return Dataset(
            table=sorted_table,
            columns=[column for column in self.columns],
            sources=self.sources,
        )

    def rename_columns(self: "Dataset", names: List[str]) -> None:
        if len(names) != len(self.columns):
            raise ValueError(
                f"Expected list with {len(self.columns)} column names"
            )
        for index, column in enumerate(self.columns):
            column.name = names[index]

    def to_pyarrow_table(self: "Dataset"):
        return self.table

    def to_pandas(self: "Dataset"):
        return self.table.to_pandas()

    def __repr__(self: "Dataset"):
        return "<ssb_datahub.Dataset>\n\nColumns:\n* " + "\n* ".join(
            column.name for column in self.columns
        )


class Client:
    """
    Client
    """

    def __init__(self: "Client"):
        # TODO: Check API availability
        # TODO: Handle user login
        ...

    def list_domains(
        self: "Client",
    ) -> List[str]:
        """
        List available domains in datahub
        """
        return [domain["name"] for domain in metadata_service.get_domains()]

    def list_products(self: "Client", domain: str):
        """
        List available products in datahub
        """
        return metadata_service.get_products_for_domain(domain)

    def get_identifier(
        self: "Client", domain: str, name: str, version: str
    ) -> Dict:
        """
        Get the json representation of an identifier in datahub
        as a python dictionary
        """
        return metadata_service.get_identifier(domain, name, version)

    def get_unit_type(self: "Client", domain: str, name: str, version: str):
        """
        Get the json representation of a unit type in datahub
        as a python dictionary
        """
        return metadata_service.get_unit_type(domain, name, version)

    def get_codelist(self: "Client", domain: str, name: str, version: str):
        """
        Get the json representation of a codelist in datahub
        as a python dictionary
        """
        return metadata_service.get_codelist(domain, name, version)

    def get_variable(
        self: "Client",
        domain: str,
        name: str,
        version: str,
        *,
        date: str = "",
        start: str = "",
        stop: str = "",
    ):
        """
        Get the variable in datahub as a datahub Dataset
        """

        def data_query_builder(
            domain: str,
            name: str,
            version: str,
            date: str,
            start: str,
            stop: str,
            temporality_type: str,
        ) -> Dict:
            return {
                "domain_name": domain,
                "variable_name": name,
                "version": version,
            }
            """
            json_query = {}
            match temporality_type:
                case "FIXED":
                    if date or start or stop:
                        raise DataQueryException(
                            "Unable to query for date, start or stop for "
                            'dataset with temporality type "FIXED"'
                        )
                case "EVENT":
                    if not start or not stop:
                        raise DataQueryException(
                            "Require a start and stop argument when querying "
                            'dataset with temporality type "EVENT"'
                        )
                    if date:
                        raise DataQueryException(
                            "Unable to query with date for dataset with "
                            'temporality type "EVENT"'
                        )
                    json_query["start"] = start
                    json_query["stop"] = stop
                case "ACCUMULATED" | "STATUS":
                    if start or stop:
                        raise DataQueryException(
                            "Unable to query with start or stop for dataset "
                            'with temporality type "STATUS" or "ACCUMULATED"'
                        )
                    if not date:
                        raise DataQueryException(
                            "Require a date argument when querying dataset with "
                            f'temporality type "{temporality_type}"'
                        )
                    json_query["date"] = date
                case _:
                    raise DataQueryException(
                        f'Invalid temporality type "{temporality_type}"'
                    )
            json_query["domainName"] = domain
            json_query["variableName"] = name
            return json_query
            """

        # get metadata
        metadata = metadata_service.get_variable(domain, name, version)
        temporality_type = metadata["temporality"]["type"]
        query = data_query_builder(
            domain, name, version, date, start, stop, temporality_type
        )
        # get data
        match temporality_type:
            case "FIXED":
                table = data_service.get_fixed(query)
                columns = [
                    Column(name="IDENTIFIER"),
                    Column(
                        name=name,
                        source=ProductReference(
                            domain=domain, name=name, version=version
                        ),
                    ),
                ]
            case "STATUS":
                table = data_service.get_status(query)
                columns = [
                    Column(
                        name="IDENTIFIER", unit_type=metadata["identifier"]
                    ),
                    Column(
                        name=name,
                        source=ProductReference(
                            domain=domain, name=name, version=version
                        ),
                    ),
                    Column(name="DATE"),
                ]
            case "ACCUMULATED":
                table = data_service.get_accumulated(query)
                columns = [
                    Column(
                        name="IDENTIFIER", unit_type=metadata["identifier"]
                    ),
                    Column(
                        name=name,
                        source=ProductReference(
                            domain=domain, name=name, version=version
                        ),
                    ),
                    Column(name="START"),
                    Column(name="STOP"),
                ]
            case "EVENT":
                table = data_service.get_event(query)
                columns = [
                    Column(
                        name="IDENTIFIER", unit_type=metadata["identifier"]
                    ),
                    Column(
                        name=name,
                        source=ProductReference(
                            domain=domain, name=name, version=version
                        ),
                    ),
                    Column(name="START"),
                    Column(name="STOP"),
                ]
            case _:
                raise DataQueryException(
                    f'Invalid temporality type "{temporality_type}"'
                )
        return Dataset(
            table=table,
            columns=columns,
            sources=[
                ProductReference(domain=domain, name=name, version=version)
            ],
        )
