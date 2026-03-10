from ._approve import Approve
from ._ban import Ban
from ._chat import Chat
from ._copy import Copy
from ._delete import Delete
from ._edit import Edit
from ._files import File
from ._forward import Forward
from ._gifts import Gifts
from ._invite import Invite
from ._message import Message
from ._mute import Mute
from ._pinned import Pinned
from ._stickers import Stickers
from ._topic import Topic
from ._webhook import Webhook
from ._downloader import Downloader

class Methods(
    Message,
    Stickers,
    Approve,
    Ban,
    Chat,
    Copy,
    Delete,
    Forward,
    Mute,
    Webhook,
    Pinned,
    File,
    Edit,
    Invite,
    Topic,
    Gifts,
    Downloader
):
    pass
