<h1 align="center">TGCore SDK</h1>
<p align="center">
A fluent DSL framework for Telegram, APIs, and AI workflows.
</p>

<p align="center">
<img src="https://img.shields.io/badge/Framework-TGCore-black?style=for-the-badge">
<img src="https://img.shields.io/badge/API-Services%20Pro-purple?style=for-the-badge">
<img src="https://img.shields.io/badge/Security-AES--256%20GCM-green?style=for-the-badge">
</p>

<p align="center">
<a href="https://github.com/TeamKillerX/tgcore">Framework TgCore</a> |
  <a href="https://teamkillerx.github.io/tgcore/docs">TeamKillerX Docs IO</a> |
  <a href="https://tgcore.ryzenths.dpdns.org">TgCore API Docs</a> |
  <a href="https://core.telegram.org/bots/api">Original Telegram API Docs</a>
  <br/><br/>
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

- [Getting Started](#getting-started)
   - [Installation](#-installation)
   - [Feature](#feature)
   - [Chain & DSL](#chain--dsl)
   - [AI Chain](#ai-chain)
   - [Traditional API](#traditional-api)
   - [TGCore Fluent Builder](#tgcore-fluent-builder)
   - [payload DSL (domain-specific language)](#payload-dsl-domain-specific-language)
   - [Clean architecture](#clean-architecture)
   - [Authentication](#-authentication)
   - [Usage](#-usage)
   - [New fluent chain API](#new-fluent-chain-api)
   - [sendMessage](#sendmessage)
   - [Simple Call](#simple-call)
   - [Builder Pattern](#builder-pattern)
   - [Rest API & TGCore Bot](#rest-api--tgcore-bot)
   - [Why TGCore?](#why-tgcore)
   - [Compared to Native Telegram API](#compared-to-native-telegram-api)
   - [License](#-license)
   - [Contributing](#-contributing)
   - [Status](#-status)
   - [Author](#-author)
 
## Feature
- Secure and scalable architecture  
- Async-first design  
- Fluent API builder pattern  
- Supports Telegram bots, APIs, and AI workflows  
- Designed for complex system composition

## 📦 Installation

`pip install tgcore`

Or install locally:

`pip install -e .`

---

## Getting started
```py
from tgcore import Client

tg = Client(api_key="YOUR_API_KEY")

await tg.raw.sendMessage()\
    .chat_id(123456789)\
    .text("Hello from TGCore")\
    .send()
```

## Chain & DSL
```py
await tg.use.default\
     .route("games", "chain")\
     .user(
         tg.where(
             name="Randy Architect",
             age="145",
             hobi="all"
         )
     )\
     .database(
         tg.where(
             mongodb=True,
             redis=True,
             sqlite=True
         )
     )\
     .pretty()
```

## AI Chain
```py
msg = tg.msg.core("Hello")

res = await tg.ai.groq()\
    .model("kimi-k2")\
    .messages([msg])\
    .send()

print(res.text())
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

## payload DSL (domain-specific language)
JSON is the output, not the source of truth
The architecture should absorb API changes

```py
result = await tg.use.default\
      .route("gemini", "gemini-2.5-flash")\
      .contents(
          [
              tg.where(
                  parts=[tg.where(text="lu siapa?")]
              )
          ]
      )\
      .system_instruction(
          tg.where(
              parts=[tg.where(text="kamu adalah TgCore komedi lucu")]
          )
      )\
      .generationConfig(
          tg.where(
              temperature=1.0,
              topP=0.8,
              topK=10
          )
      )\
      .send()

return result.text()
```

## Clean architecture
* Architecture: clean
* Code: perfect
* Async: working

```py
tg = Client(api_key="something", base_url="https://your_domain.com")

result = await tg.use.default\
    .endpoint("/v1/chat/completions")\
    .model("model")\
    .messages([...])\
    .stream(False)\
    .send()

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

Built with ❤️ by [Randy W](https://t.me/zxyeor)
