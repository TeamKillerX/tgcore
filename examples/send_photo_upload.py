# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
# pylint: disable=too-many-public-methods
# pylint: disable=line-too-long
# pylint: disable=protected-access
# pylint: disable=undefined-variable
# pylint: disable=too-few-public-methods
# pylint: disable=invalid-name

with open("new_image.jpg", "rb") as f:
    await tg._post("/api/v2/sendPhoto/upload", {
        "chat_id": m.chat.id,
        "photo": ("a.jpg", f, "image/jpeg"),
        "caption": "ok",
        "reply_markup": KeyboardBuilder().url("testing", "https://github.com/TeamKillerX/tgcore").build()
    })
