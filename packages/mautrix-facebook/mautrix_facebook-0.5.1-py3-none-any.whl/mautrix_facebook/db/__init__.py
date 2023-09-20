from mautrix.util.async_db import Database

from .backfill_queue import Backfill
from .message import Message
from .portal import Portal, ThreadType
from .puppet import Puppet
from .reaction import Reaction
from .upgrade import upgrade_table
from .user import User
from .user_portal import UserPortal


def init(db: Database) -> None:
    for table in (Portal, Message, Reaction, User, Puppet, UserPortal, Backfill):
        table.db = db


__all__ = [
    "upgrade_table",
    "init",
    "Backfill",
    "Message",
    "Reaction",
    "Portal",
    "ThreadType",
    "Puppet",
    "User",
    "UserPortal",
]
