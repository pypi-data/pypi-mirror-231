from . import get_uow_info
from .init import _load_cruise_files, _load_cruise_metadata, _write_uow_cache


def do_refresh():
    """Load all the uow info contents again from the CCHDO API."""
    uow_info, dir_name = get_uow_info()
    cruise_id = uow_info["cruise_id"]
    cruise_metadata = _load_cruise_metadata(cruise_id)
    cruise_files = _load_cruise_files(cruise_id)
    _write_uow_cache(dir_name, cruise_id, cruise_metadata, cruise_files)
