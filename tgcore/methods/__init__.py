from .approve import Approve
from .ban import Ban
from .chat import Chat
from .copy import Copy
from .deletemsg import DeleteMsg
from .edit import Edit
from .files import File
from .forward import Forward
from .gifts import Gifts
from .invite import Invite
from .message import Message
from .mute import Mute
from .pinned import Pinned
from .stickers import Stickers
from .topic import Topic
from .webhook import Webhook


class Methods(
    Message,
    Stickers,
    Approve,
    Ban,
    Chat,
    Copy,
    DeleteMsg,
    Forward,
    Mute,
    Webhook,
    Pinned,
    File,
    Edit,
    Invite,
    Topic,
    Gifts
):
    pass
