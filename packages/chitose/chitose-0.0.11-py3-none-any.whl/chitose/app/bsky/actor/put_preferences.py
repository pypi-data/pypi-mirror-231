# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs

def _put_preferences(call: chitose.xrpc.XrpcCall, preferences: chitose.app.bsky.actor.defs.Preferences) -> bytes:
    """Sets the private preferences attached to the account."""
    return call('app.bsky.actor.putPreferences', [], {'preferences': preferences}, {'Content-Type': 'application/json'})