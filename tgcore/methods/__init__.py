from .message import Message
from .stickers import Stickers
from .approve import Approve
from .ban import Ban
from .chat import Chat
from .copy import Copy
from .deletemsg import DeleteMsg
from .forward import Forward
from .mute import Mute
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
    Webhook
):
    pass
