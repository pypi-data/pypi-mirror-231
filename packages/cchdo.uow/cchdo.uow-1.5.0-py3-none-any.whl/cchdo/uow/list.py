import jq
from rich.table import Table

from . import get_uow_info
from .console import console

table_headers = (
    "id",
    "role",
    "data type",
    "data format",
    "last submit date",
    "last submit by",
    "file name",
)


def _get_list_row(id, file_meta):
    row = []
    row.append(str(id))
    row.append(file_meta["role"])
    row.append(file_meta["data_type"])
    row.append(file_meta["data_format"])
    if len(file_meta["submissions"]) > 0:
        row.append(file_meta["submissions"][0]["date"])
        row.append(file_meta["submissions"][0]["name"])
    else:
        row.append("")
        row.append("")
    row.append(file_meta["file_name"])
    return row


def _print_file_list(uow_info, key, query, raw=False, internal=False):
    table = Table(title="Files attached to the Cruise")
    for column in table_headers:
        table.add_column(column)

    files = [{"id": int(id), **file} for id, file in uow_info["file_metadata"].items()]

    if query is None:
        if key == "all":
            query = "."
        elif key == "other":
            query = '.role=="dataset" or .role=="unprocessed" or .role=="merged"|not'
        else:
            query = f'.role=="{key}"'

    result = jq.compile(f".[] | select({query})").input_value(files).all()

    if internal:
        return result

    if raw:
        console.print_json(data=result)
        return

    for file in result:
        row = _get_list_row(file["id"], file)
        table.add_row(*row)

    if table.row_count > 0:
        console.print(table)
    else:
        console.print("No Files")


def do_list(list_option, query, raw):
    """List files available for fetching"""
    uow_info, _ = get_uow_info()
    _print_file_list(uow_info, list_option, query, raw)
