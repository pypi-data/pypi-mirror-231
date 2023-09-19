# GENERATED CODE - DO NOT MODIFY
from __future__ import annotations
from chitose.xrpc import XrpcCall
from chitose.xrpc import XrpcSubscribe
from .get_unread_count import _get_unread_count
from .list_notifications import _list_notifications
from .register_push import _register_push
from .update_seen import _update_seen
import typing

class Notification_:
    """We recommend calling methods in this class via the :doc:`chitose.BskyAgent <chitose>` class instead of creating instances of this class directly."""

    def __init__(self, call: XrpcCall, subscribe: XrpcSubscribe) -> None:
        self.call = call
        self.subscribe = subscribe

    def register_push(self, service_did: str, token: str, platform: typing.Literal['ios', 'android', 'web'], app_id: str) -> bytes:
        """Register for push notifications with a service"""
        return _register_push(self.call, service_did, token, platform, app_id)

    def update_seen(self, seen_at: str) -> bytes:
        """Notify server that the user has seen notifications."""
        return _update_seen(self.call, seen_at)

    def list_notifications(self, limit: typing.Optional[int]=None, cursor: typing.Optional[str]=None, seen_at: typing.Optional[str]=None) -> bytes:
        """"""
        return _list_notifications(self.call, limit, cursor, seen_at)

    def get_unread_count(self, seen_at: typing.Optional[str]=None) -> bytes:
        """"""
        return _get_unread_count(self.call, seen_at)