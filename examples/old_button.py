# old version: 1.0.14
from tgcore import Client, KeyboardBuilder

tg = Client()

async def use_pyrogram(m):
    await tg.telegram.send_message(
        chat_id=str(m.chat.id),
        text="This Button",
        reply_markup=(
            KeyboardBuilder()
            .row("GitHub", url="https://github.com")
            .row("Docs", url="https://www.learnpython.org/")
            .row("Pypi", url="https://pypi.org/project/tgcore/")
            .build()
        )
