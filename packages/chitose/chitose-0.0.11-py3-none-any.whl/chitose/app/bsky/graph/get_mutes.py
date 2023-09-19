# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import typing

def _get_mutes(call: chitose.xrpc.XrpcCall, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None) -> bytes:
    """Who does the viewer mute?"""
    return call('app.bsky.graph.getMutes', [('limit', limit), ('cursor', cursor)], None, {})