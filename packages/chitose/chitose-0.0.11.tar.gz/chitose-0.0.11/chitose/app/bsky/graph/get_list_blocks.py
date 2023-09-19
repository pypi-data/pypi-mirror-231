# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_list_blocks(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Which lists is the requester's account blocking?"""
    return call('app.bsky.graph.getListBlocks', [('limit', limit), ('cursor', cursor)], None, {})