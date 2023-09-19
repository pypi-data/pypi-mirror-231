import importlib.metadata

__version__ = importlib.metadata.version(__package__ or __name__)

from albertai.apps.App import App  # noqa: F401
from albertai.apps.CustomApp import CustomApp  # noqa: F401
from albertai.apps.Llama2App import Llama2App  # noqa: F401
from albertai.apps.OpenSourceApp import OpenSourceApp  # noqa: F401
from albertai.apps.PersonApp import (PersonApp,  # noqa: F401
                                       PersonOpenSourceApp)
