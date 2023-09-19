""" Remote Grants

Fakts remote grants are used to retrieve configuration from a remote endpoint. 
All this grants are based on the Fakts Registration Protocol that tries to ensure
legitmitate registration of apps on a dynamic endpoint



"""

from .base import RemoteGrant
from .types import Demander, Discovery, FaktsEndpoint


__all__ = ["RemoteGrant", "Demander", "Discovery", "FaktsEndpoint"]
