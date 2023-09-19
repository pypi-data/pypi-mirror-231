# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose

def _resolve_handle(call: chitose.xrpc.XrpcCall, handle: str) -> bytes:
    """Provides the DID of a repo.


    :param handle: The handle to resolve.
    """
    return call('com.atproto.identity.resolveHandle', [('handle', handle)], None, {})