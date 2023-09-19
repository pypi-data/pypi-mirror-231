# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs
import typing

def _get_likes(call: chitose.xrpc.XrpcCall, uri: str, cid: typing.Optional[str]=None, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """"""
    return call('app.bsky.feed.getLikes', [('uri', uri), ('cid', cid), ('limit', limit), ('cursor', cursor)], None, {})

class Like(chitose.Object):
    """"""

    def __init__(self, indexed_at: str, created_at: str, actor: chitose.app.bsky.actor.defs.ProfileView) -> None:
        self.indexed_at = indexed_at
        self.created_at = created_at
        self.actor = actor

    def to_dict(self) -> dict[str, typing.Any]:
        return {'indexedAt': self.indexed_at, 'createdAt': self.created_at, 'actor': self.actor, '$type': 'app.bsky.feed.getLikes#like'}