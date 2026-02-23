# version: 1.0.30

from tgcore import Client

tg = Client()

async def chat_title(chat_id):
    await tg.raw.setChatTitle(
        chat_id=chat_id,
        title="New chat title"
    ).execute()
