# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.richtext.facet
import typing

class Facet(chitose.Object):
    """"""

    def __init__(self, index: chitose.app.bsky.richtext.facet.ByteSlice, features: list[typing.Union[chitose.app.bsky.richtext.facet.Mention, chitose.app.bsky.richtext.facet.Link]]) -> None:
        self.index = index
        self.features = features

    def to_dict(self) -> dict[str, typing.Any]:
        return {'index': self.index, 'features': self.features, '$type': 'app.bsky.richtext.facet'}

class Mention(chitose.Object):
    """A facet feature for actor mentions."""

    def __init__(self, did: str) -> None:
        self.did = did

    def to_dict(self) -> dict[str, typing.Any]:
        return {'did': self.did, '$type': 'app.bsky.richtext.facet#mention'}

class Link(chitose.Object):
    """A facet feature for links."""

    def __init__(self, uri: str) -> None:
        self.uri = uri

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, '$type': 'app.bsky.richtext.facet#link'}

class ByteSlice(chitose.Object):
    """A text segment. Start is inclusive, end is exclusive. Indices are for utf8-encoded strings."""

    def __init__(self, byte_start: int, byte_end: int) -> None:
        self.byte_start = byte_start
        self.byte_end = byte_end

    def to_dict(self) -> dict[str, typing.Any]:
        return {'byteStart': self.byte_start, 'byteEnd': self.byte_end, '$type': 'app.bsky.richtext.facet#byteSlice'}