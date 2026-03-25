# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=undefined-variable
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

# version: 1.0.29

from tgcore import ChatPermissions as ChatPermissionsBuilder
from tgcore import Client

tg = Client()

async def chat_group(chat_id):
    """
    can_send_messages
    can_send_audios,
    can_send_documents,
    can_send_photos,
    can_send_videos,
    can_send_video_notes,
    can_send_voice_notes
    can_send_polls
    can_send_other_messages
    can_add_web_page_previews
    can_change_info
    can_pin_messages
    can_manage_topics

    Pass True if chat permissions are set independently.
    use_independent_chat_permissions=True
    """
    await tg.raw.setChatPermissions(
        chat_id=chat_id,
        permissions=(
            ChatPermissionsBuilder()
            .can_send_messages(False)
            .build()
        )
    ).execute()
