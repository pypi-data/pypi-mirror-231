import os

from rich.table import Table

from . import get_fetch_events, get_uow_info
from .commit import _prepare_api_calls
from .console import console
from .uow_json import load_uow_json


def _check_fetched_file_status(event, fetch_path):
    """Performes some very basic checks:
    1) Does the file exist?
    2) Is the file the same size?

    If the file exists and is the same size, assume ok.
    If the file exists and is a different size, assume modified
    If the file does not exists (or has been renamed) assume deleted

    Note that if a file has been modified but the size is the same, this method
    will return OK. This is because to check the actual difference we would
    need to hash the file (which can take a very long time) or keep a copy of
    the fetched file somewhere away from the user to compare.
    """
    expected_size = event["file_size"]

    file_exists = os.path.exists(fetch_path)

    if file_exists and os.path.getsize(fetch_path) == expected_size:
        return "[green]OK"
    elif file_exists:
        return "[yellow]MODIFIED"
    else:
        return "[red]DELETED"


def _print_fetch_events_table(events):
    table = []
    table = Table(title="Fetched Files")
    table.add_column("id", justify="right", no_wrap=True)
    table.add_column("Status")
    table.add_column("File Path")

    for event in events:
        fetch_name = f"{event['id']}_{event['file_name']}"
        fetch_path = os.path.join("0.existing_files", fetch_name)

        file_status = _check_fetched_file_status(event, fetch_path)

        table.add_row(str(event["id"]), file_status, fetch_path)

    if table.row_count > 0:
        console.print(table)
        console.print(
            "[green]OK[/green]: The file present and seems fine\n"
            "[yellow]MODIFIED[/yellow]: The file appears to be modified, a commit using this "  # noqa: E501
            "file will not likly succeed, fetch it again to fix\n"
            "[red]DELETED[/red]: The file is no longer present on the system or has been "  # noqa: E501
            "renamed, if not using a deleted file for a commit, just ignore"
        )
    else:
        console.print("No Files Fetched")


def _print_new_files_table():
    _, basedir = get_uow_info()
    table = Table(title="New Files")
    table.add_column("File Name")
    for _, _, fils in os.walk(os.path.join(basedir, "1.new_files")):
        for file in fils:
            if file.startswith("."):
                continue
            table.add_row(file)
        break
    if table.row_count > 0:
        console.print(table)
    else:
        console.print("No new files (in 1.new_files)")


def do_status():
    """Print the status of a uow directory"""
    config, _ = get_uow_info()
    fetch_events = get_fetch_events()
    _print_fetch_events_table(fetch_events)
    _print_new_files_table()
    uow_json = load_uow_json()
    console.print("\nWhat would happen if a commit was done (may take a while):")
    _prepare_api_calls(uow_json, fetch_events, for_human=True)
    console.print(
        f"\n All files the note would be attached to the cruise id: {config['cruise_id']}"  # noqa: E501
    )
