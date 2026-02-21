with open("new_image.jpg", "rb") as f:
    await tg._post("/api/v2/sendPhoto/upload", {
        "chat_id": m.chat.id,
        "photo": ("a.jpg", f, "image/jpeg"),
        "caption": "ok",
        "reply_markup": KeyboardBuilder().url("testing", "https://github.com/TeamKillerX/tgcore").build()
    })
