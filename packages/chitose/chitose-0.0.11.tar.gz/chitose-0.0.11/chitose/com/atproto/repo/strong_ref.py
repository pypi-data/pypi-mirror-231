# GENERATED CODE - DO NOT MODIFY
"""A URI with a content-hash fingerprint."""
from __future__ import annotations
import chitose
import typing

class StrongRef(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str) -> None:
        self.uri = uri
        self.cid = cid

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, '$type': 'com.atproto.repo.strongRef'}