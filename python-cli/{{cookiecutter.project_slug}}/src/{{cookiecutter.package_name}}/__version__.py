import logging
import importlib.metadata


try:
    __version__ = importlib.metadata.version("{{cookiecutter.project_slug}}")
except importlib.metadata.PackageNotFoundError:
    logging.warning("Can not read version from pyproject.toml. Set it to 'unknown' value.")
    __version__ = "unknown"