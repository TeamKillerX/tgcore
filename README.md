# TgCoreSDK • Async Telegram API Client Framework

TgCoreSDK is a modern, asynchronous-based, developer-friendly SDK designed to interact with the Telegram Bot API through a secure gateway layer.
Built for performance, extensibility


##  ✨ Features

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

Simple Call
```py
await client.telegram.send_message(
    chat_id="@channel",
    text="Hello world"
)
```
---

Builder Pattern
```py
await (
    client.telegram
        .send_photo_call(chat_id="@channel", photo="https://img.jpg")
        .execute()
)
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
