# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=undefined-variable
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

# version: 1.0.30

from tgcore import Client

tg = Client()

async def chat_title(chat_id):
    await tg.raw.setChatTitle(
        chat_id=chat_id,
        title="New chat title"
    ).execute()
