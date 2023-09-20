""" A client library for accessing Sparkfly """
from .__version__ import __author__, __email__, __version__
from .client import AuthenticatedClient, Client

__all__ = (
    "AuthenticatedClient",
    "Client",
    "__author__",
    "__email__",
    "__version__"
)
