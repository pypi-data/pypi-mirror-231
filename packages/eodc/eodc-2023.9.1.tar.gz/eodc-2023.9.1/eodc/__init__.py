import importlib.metadata

__version__ = importlib.metadata.version("eodc")

from eodc.settings import settings  # noqa

from . import dask, faas, storage, workspace  # noqa
