<h1 align="center">TGCore SDK</h1>
<p align="center">
Enterprise Telegram Bot Framework • Secure • Scalable • Zero-Trust Ready
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
![Python](https://img.shields.io/badge/Python-3.8+-blue)
![License](https://img.shields.io/badge/License-Apache%202.0-green)

The most secure Telegram Bot SDK ever built.

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
