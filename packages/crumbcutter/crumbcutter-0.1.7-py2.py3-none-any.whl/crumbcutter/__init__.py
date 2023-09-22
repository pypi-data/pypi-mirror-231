# ./crumbcutter/__init__.py
"""__init__.py for crumbcutter package."""
from pathlib import Path


def _get_version() -> str:
    """Read VERSION.txt and return its contents."""
    path = Path(__file__).parent.resolve()
    version_file = path / "VERSION.txt"
    return version_file.read_text().strip()


__version__ = _get_version()

from .cli import cli
from .crumbcutter import extract_content_from_gist, fetch_gist, main, validate_gist, validate_username_gistname_pair
