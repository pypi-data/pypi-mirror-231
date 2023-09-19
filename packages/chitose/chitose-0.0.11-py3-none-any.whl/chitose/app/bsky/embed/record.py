# GENERATED CODE - DO NOT MODIFY
"""A representation of a record embedded in another form of content"""
from __future__ import annotations
import chitose
import chitose.app.bsky.actor.defs
import chitose.app.bsky.embed.external
import chitose.app.bsky.embed.images
import chitose.app.bsky.embed.record
import chitose.app.bsky.embed.record_with_media
import chitose.app.bsky.feed.defs
import chitose.app.bsky.graph.defs
import chitose.com.atproto.label.defs
import chitose.com.atproto.repo.strong_ref
import typing

class Record(chitose.Object):
    """"""

    def __init__(self, record: chitose.com.atproto.repo.strong_ref.StrongRef) -> None:
        self.record = record

    def to_dict(self) -> dict[str, typing.Any]:
        return {'record': self.record, '$type': 'app.bsky.embed.record'}

class View(chitose.Object):
    """"""

    def __init__(self, record: typing.Union[chitose.app.bsky.embed.record.ViewRecord, chitose.app.bsky.embed.record.ViewNotFound, chitose.app.bsky.embed.record.ViewBlocked, chitose.app.bsky.feed.defs.GeneratorView, chitose.app.bsky.graph.defs.ListView]) -> None:
        self.record = record

    def to_dict(self) -> dict[str, typing.Any]:
        return {'record': self.record, '$type': 'app.bsky.embed.record#view'}

class ViewRecord(chitose.Object):
    """"""

    def __init__(self, uri: str, cid: str, author: chitose.app.bsky.actor.defs.ProfileViewBasic, value: typing.Any, indexed_at: str, labels: typing.Optional[list[chitose.com.atproto.label.defs.Label]]=None, embeds: typing.Optional[list[typing.Union[chitose.app.bsky.embed.images.View, chitose.app.bsky.embed.external.View, chitose.app.bsky.embed.record.View, chitose.app.bsky.embed.record_with_media.View]]]=None) -> None:
        self.uri = uri
        self.cid = cid
        self.author = author
        self.value = value
        self.indexed_at = indexed_at
        self.labels = labels
        self.embeds = embeds

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'cid': self.cid, 'author': self.author, 'value': self.value, 'indexedAt': self.indexed_at, 'labels': self.labels, 'embeds': self.embeds, '$type': 'app.bsky.embed.record#viewRecord'}

class ViewNotFound(chitose.Object):
    """"""

    def __init__(self, uri: str, not_found: bool) -> None:
        self.uri = uri
        self.not_found = not_found

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'notFound': self.not_found, '$type': 'app.bsky.embed.record#viewNotFound'}

class ViewBlocked(chitose.Object):
    """"""

    def __init__(self, uri: str, blocked: bool, author: chitose.app.bsky.feed.defs.BlockedAuthor) -> None:
        self.uri = uri
        self.blocked = blocked
        self.author = author

    def to_dict(self) -> dict[str, typing.Any]:
        return {'uri': self.uri, 'blocked': self.blocked, 'author': self.author, '$type': 'app.bsky.embed.record#viewBlocked'}