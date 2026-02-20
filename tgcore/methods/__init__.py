from .approve import Approve
from .ban import Ban
from .chat import Chat
from .copy import Copy
from .deletemsg import DeleteMsg
from .files import File
from .forward import Forward
from .message import Message
from .mute import Mute
from .pinned import Pinned
from .stickers import Stickers
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
    File
):
    pass
