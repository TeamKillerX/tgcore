# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=undefined-variable
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

# Latest version 1.0.16+
# Support Pyrogram/Kurigram (KeyboardBuilder)

from tgcore import Client, KeyboardBuilder

tg = Client()

async def send():
    await (
        tg.raw
        .sendMessage(
            chat_id=m.chat.id,
            text="Testing",
            reply_markup=(
                KeyboardBuilder()
                .url("This Url", "https://github.com/TeamKillerX/tgcore")
                .style("This color", "danger", callback_data="#abc")
                .build()
            )
        )
        .execute()
    )
