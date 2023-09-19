# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.app.bsky.embed.external
import chitose.app.bsky.embed.images
import chitose.app.bsky.embed.record
import chitose.app.bsky.embed.record_with_media
import chitose.app.bsky.feed.post
import chitose.app.bsky.richtext.facet
import chitose.com.atproto.label.defs
import chitose.com.atproto.repo.strong_ref
import typing

class Post(chitose.Record):
    """


    :param entities: Deprecated: replaced by app.bsky.richtext.facet.
    """

    def __init__(self, text: str, created_at: str, entities: typing.Optional[list[chitose.app.bsky.feed.post.Entity]]=None, facets: typing.Optional[list[chitose.app.bsky.richtext.facet.Facet]]=None, reply: typing.Optional[chitose.app.bsky.feed.post.ReplyRef]=None, embed: typing.Optional[typing.Union[chitose.app.bsky.embed.images.Images, chitose.app.bsky.embed.external.External, chitose.app.bsky.embed.record.Record, chitose.app.bsky.embed.record_with_media.RecordWithMedia]]=None, langs: typing.Optional[list[str]]=None, labels: typing.Optional[chitose.com.atproto.label.defs.SelfLabels]=None) -> None:
        self.text = text
        self.created_at = created_at
        self.entities = entities
        self.facets = facets
        self.reply = reply
        self.embed = embed
        self.langs = langs
        self.labels = labels

    def to_dict(self) -> dict[str, typing.Any]:
        return {'text': self.text, 'createdAt': self.created_at, 'entities': self.entities, 'facets': self.facets, 'reply': self.reply, 'embed': self.embed, 'langs': self.langs, 'labels': self.labels, '$type': 'app.bsky.feed.post'}

class ReplyRef(chitose.Object):
    """"""

    def __init__(self, root: chitose.com.atproto.repo.strong_ref.StrongRef, parent: chitose.com.atproto.repo.strong_ref.StrongRef) -> None:
        self.root = root
        self.parent = parent

    def to_dict(self) -> dict[str, typing.Any]:
        return {'root': self.root, 'parent': self.parent, '$type': 'app.bsky.feed.post#replyRef'}

class Entity(chitose.Object):
    """Deprecated: use facets instead.


    :param type: Expected values are 'mention' and 'link'.
    """

    def __init__(self, index: chitose.app.bsky.feed.post.TextSlice, type: str, value: str) -> None:
        self.index = index
        self.type = type
        self.value = value

    def to_dict(self) -> dict[str, typing.Any]:
        return {'index': self.index, 'type': self.type, 'value': self.value, '$type': 'app.bsky.feed.post#entity'}

class TextSlice(chitose.Object):
    """Deprecated. Use app.bsky.richtext instead -- A text segment. Start is inclusive, end is exclusive. Indices are for utf16-encoded strings."""

    def __init__(self, start: int, end: int) -> None:
        self.start = start
        self.end = end

    def to_dict(self) -> dict[str, typing.Any]:
        return {'start': self.start, 'end': self.end, '$type': 'app.bsky.feed.post#textSlice'}