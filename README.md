<h1 align="center">TGCore SDK</h1>
<p align="center">
Enterprise Telegram Bot Framework • Secure • Scalable • Zero-Trust Ready • Python Telegram Bot SDK • Telegram Bot Framework for Python • Fluent API Builder Pattern • Async Telegram Bot Framework • Telegram Bot Architecture Design
</p>

<p align="center">
<img src="https://img.shields.io/badge/Framework-TGCore-black?style=for-the-badge">
<img src="https://img.shields.io/badge/API-Services%20Pro-purple?style=for-the-badge">
<img src="https://img.shields.io/badge/Security-AES--256%20GCM-green?style=for-the-badge">
</p>

![Maintained](https://img.shields.io/badge/maintained-yes-success?style=flat-square)
![PRs](https://img.shields.io/badge/PRs-welcome-brightgreen?style=flat-square)
![Security](https://img.shields.io/badge/security-audited-blue?style=flat-square)
![Architecture](https://img.shields.io/badge/architecture-clean-lightgrey?style=flat-square)
![FastAPI](https://img.shields.io/badge/backend-FastAPI-05998b?style=flat-square)
![MongoDB](https://img.shields.io/badge/database-MongoDB-4ea94b?style=flat-square)
![Async](https://img.shields.io/badge/async-native-orange?style=flat-square)
![Webhook](https://img.shields.io/badge/webhook-supported-blueviolet?style=flat-square)
![tgcore](https://img.shields.io/badge/TGCore-SDK-black)

[![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit)](https://github.com/pre-commit/pre-commit)
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![PyPI](https://img.shields.io/pypi/v/tgcore?style=for-the-badge)
![Downloads](https://img.shields.io/pypi/dm/tgcore?style=for-the-badge)
![Python](https://img.shields.io/pypi/pyversions/tgcore?style=for-the-badge)

![License](https://img.shields.io/pypi/l/tgcore)

Security-focused Telegram Bot Framework.

##  ✨ Features
- 🧩 Fluent builder API
- 🧲 Keyboard builder
- 🪄 AI integrations
- 📥 Platform downloader
- ⚡ Async native ("async/await")
- 🔐 Secure API key authentication
- 🤖 Multi-bot token support
- 🔁 Token rotation ready
- 🧩 Builder pattern + simple calls
- 📦 Auto-generated methods from OpenAPI schema
- 📚 Auto docstring generation
- 🏗 Enterprise-ready architecture

---

## 📦 Installation

`pip install tgcore`

Or install locally:

`pip install -e .`

---

## Quick Start Code
```py
from tgcore import Client

tg = Client(api_key="YOUR_API_KEY")

await tg.raw.sendMessage()\
    .chat_id(123456789)\
    .text("Hello from TGCore")\
    .send()
```

## Traditional API
```py
send_message(
    chat_id,
    text,
    parse_mode,
    disable_notification,
    reply_markup,
    protect_content
)
```
## TGCore Fluent Builder
```py
send_message()\
    .chat_id(id)\
    .text("hello")\
    .send()
```

## Clean architecture
* Architecture: clean
* Code: perfect
* Async: working

```py
tg = Client(api_key="something", base_url="https://your_domain.com")

result = await tg.use.default\
    .types("/v1/chat/completions", use=True)\
    .model("model")\
    .messages([...])\
    .stream(False)\
    .send(allow_object=True)

print(result)
```

## 🔑 Authentication

Create client instance:
```py
from tgcore import Client

client = Client("fw_live_xxx")

await client.telegram.send_message(
    chat_id="@channel",
    text="hello"
)
```
---

## 👾 Usage
### Platform Tools
```py
resp = await tg.platform.facebook\
    .download(url="https://facebook.com/...")\
    .send()
```
### New fluent chain API

Parameters can be chained (`builder-style`) without having to write long functions like `send_message(...)`.

- Platform Downloader (7-day free trial)
- `/api/web/facebook/download`
- `/api/web/tiktok/download`
- `/api/web/pinterest/download`

Example of using fluent chain API:
```py
# version: 1.0.43+, 1.0.68+
async def full_code():
    _ = await tg.fetch_post(
        "/api/web/facebook/download",
        url="https://www.facebook.com/groups/788889186033999/permalink/1325624742360438/?app=fbl",
        check_errors=True
    )
    await tg.raw\
    .sendVideo()\
    .chat_id(chat_id)\
    .video(_.data.video[0].url)\
    .reply_markup(
        tg.kb().copy_text(
            "this SDK builder style",
            "use a framework"
        )
        .build()
    )\
    .skip()
```
Example:
`await tg.raw.sendMessage().chat_id(chat_id).text("tgcore").skip()`

That's the concept of builder + fluent chain API.

### sendMessage
```py
# Latest version 1.0.16+, 1.0.68+
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
```

### New button
```py
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
```

### Simple Call
```py
await client.telegram.send_message(
    chat_id="@channel",
    text="Hello world"
)
```
---

### Builder Pattern
```py
await (
    client.telegram
        .send_photo_call(chat_id="@channel", photo="https://img.jpg")
        .execute()
)
```

### Rest API & TgCore Bot
```py
# Version: 1.0.68+
from tgcore import Client, KeyboardBuilder

tg = Client()

async def pinterest_images(q: str):
    kw = await tg._post(
        "/api/web/pinterest",
        payload={"query": q}
    )
    like_ts = tg.to_obj(kw)
    if not like_ts.ok or not like_ts.data:
        return None
    return like_ts.data.pins[1].media.images.orig.url

async def send_photo():
    newurl = await pinterest_images("Real coding")
    resp = await tg.raw.sendPhoto(
        chat_id=-100123456789,
        photo=newurl,
        reply_markup=(
            KeyboardBuilder()
            .url("View Pinterest", newurl)
            .url("Tgcore on PyPI", "https://pypi.org/project/tgcore/")
            .row()
            .url("Tgcore on NPMJS", "https://www.npmjs.com/package/@xtsea/tgcore-ts")
            .build()
        )
    ).execute()
    return tg.to_obj(resp).ok
```
---

## 🔄 Token Rotation Support

The server supports storing encrypted tokens using AES-256-GCM.
The SDK automatically uses the active token version.

## 🔒 Security Model

TgCoreSDK never exposes bot tokens to clients.

Flow:

Client → API Gateway → Decrypt → Telegram API

Benefits:

- prevents token leaks
- safe frontend usage
- safe monitoring dashboards
- supports IP restrictions

---

## Why TGCore?

Unlike traditional Telegram SDKs, TGCore is built as a **secure middleware layer** that prevents token leaks, enforces API-key auth, and supports enterprise-grade scaling.

Designed for production, not demos.

## Compared to Native Telegram API

| Feature | Telegram API | TGCore |
|-------|--------------|--------|
Token Exposure | Yes | No |
Auth Layer | None | API Key + Secret |
Proxy Support | Manual | Built-in |
Multi Bot | Limited | Yes |
Webhook Security | Basic | Zero-Trust |

## 🧾 License

Licensed under Apache License 2.0

You may:

- use commercially
- modify
- distribute
- sublicense

---

## 🤝 Contributing

Pull requests welcome.
For major changes, open an issue first to discuss what you would like to change.

---

## 🔥 Status

Production Ready

---

## 👑 Author

Built with ❤️ by Randy W
