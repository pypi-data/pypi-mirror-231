# GENERATED CODE - DO NOT MODIFY
""""""
from __future__ import annotations
import chitose
import chitose.com.atproto.sync.subscribe_repos
import typing

def _subscribe_repos(subscribe: chitose.xrpc.XrpcSubscribe, handler: chitose.xrpc.XrpcHandler, cursor: typing.Optional[int]=None) -> None:
    """Subscribe to repo updates


    :param cursor: The last known event to backfill from.
    """
    subscribe('com.atproto.sync.subscribeRepos', [('cursor', cursor)], handler)

class Commit(chitose.Object):
    """


    :param rev: The rev of the emitted commit

    :param since: The rev of the last emitted commit from this repo

    :param blocks: CAR file containing relevant blocks
    """

    def __init__(self, seq: int, rebase: bool, too_big: bool, repo: str, commit: typing.Any, rev: str, since: str, blocks: typing.Any, ops: list[chitose.com.atproto.sync.subscribe_repos.RepoOp], blobs: list[typing.Any], time: str, prev: typing.Optional[typing.Any]=None) -> None:
        self.seq = seq
        self.rebase = rebase
        self.too_big = too_big
        self.repo = repo
        self.commit = commit
        self.rev = rev
        self.since = since
        self.blocks = blocks
        self.ops = ops
        self.blobs = blobs
        self.time = time
        self.prev = prev

    def to_dict(self) -> dict[str, typing.Any]:
        return {'seq': self.seq, 'rebase': self.rebase, 'tooBig': self.too_big, 'repo': self.repo, 'commit': self.commit, 'rev': self.rev, 'since': self.since, 'blocks': self.blocks, 'ops': self.ops, 'blobs': self.blobs, 'time': self.time, 'prev': self.prev, '$type': 'com.atproto.sync.subscribeRepos#commit'}

class Handle(chitose.Object):
    """"""

    def __init__(self, seq: int, did: str, handle: str, time: str) -> None:
        self.seq = seq
        self.did = did
        self.handle = handle
        self.time = time

    def to_dict(self) -> dict[str, typing.Any]:
        return {'seq': self.seq, 'did': self.did, 'handle': self.handle, 'time': self.time, '$type': 'com.atproto.sync.subscribeRepos#handle'}

class Migrate(chitose.Object):
    """"""

    def __init__(self, seq: int, did: str, migrate_to: str, time: str) -> None:
        self.seq = seq
        self.did = did
        self.migrate_to = migrate_to
        self.time = time

    def to_dict(self) -> dict[str, typing.Any]:
        return {'seq': self.seq, 'did': self.did, 'migrateTo': self.migrate_to, 'time': self.time, '$type': 'com.atproto.sync.subscribeRepos#migrate'}

class Tombstone(chitose.Object):
    """"""

    def __init__(self, seq: int, did: str, time: str) -> None:
        self.seq = seq
        self.did = did
        self.time = time

    def to_dict(self) -> dict[str, typing.Any]:
        return {'seq': self.seq, 'did': self.did, 'time': self.time, '$type': 'com.atproto.sync.subscribeRepos#tombstone'}

class Info(chitose.Object):
    """"""

    def __init__(self, name: typing.Literal['OutdatedCursor',], message: typing.Optional[str]=None) -> None:
        self.name = name
        self.message = message

    def to_dict(self) -> dict[str, typing.Any]:
        return {'name': self.name, 'message': self.message, '$type': 'com.atproto.sync.subscribeRepos#info'}

class RepoOp(chitose.Object):
    """A repo operation, ie a write of a single record. For creates and updates, cid is the record's CID as of this operation. For deletes, it's null."""

    def __init__(self, action: typing.Literal['create', 'update', 'delete'], path: str, cid: typing.Any) -> None:
        self.action = action
        self.path = path
        self.cid = cid

    def to_dict(self) -> dict[str, typing.Any]:
        return {'action': self.action, 'path': self.path, 'cid': self.cid, '$type': 'com.atproto.sync.subscribeRepos#repoOp'}