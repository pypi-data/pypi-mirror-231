# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _list_app_passwords(call: chitose.xrpc.XrpcCall) -> bytes:
    """List all app-specific passwords."""
    return call('com.atproto.server.listAppPasswords', [], None, {})

class AppPassword(chitose.Object):
    """"""

    def __init__(self, name: str, created_at: str) -> None:
        self.name = name
        self.created_at = created_at

    def to_dict(self) -> dict[str, typing.Any]:
        return {'name': self.name, 'createdAt': self.created_at, '$type': 'com.atproto.server.listAppPasswords#appPassword'}