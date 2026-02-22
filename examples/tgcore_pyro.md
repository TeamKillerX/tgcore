# Pyrogram Bot + Userbot Integration with tgcore

A modular Telegram architecture combining Pyrogram event handling with tgcore execution power.

```python
from tgcore import KeyboardBuilder, ReplyParametersBuilder
from pyrogram import Client, filters

@Client.on_message(
    ~filters.scheduled
    & filters.command(["start"])
    & ~filters.forwarded
)
async def start_command(client, message) -> None:
    await client.tg.raw.sendMessage(
        chat_id=message.chat.id,
        text="Hello World",
        reply_parameters=(
            ReplyParametersBuilder()
            .message_id(message.id)
            .build()
        ),
        reply_markup=(
            KeyboardBuilder()
            .url("Google", "https://google.com")
            .build()
        )
    ).execute()
```

## Architecture Overview

| Component | Implementation |
|-----------|---------------|
| **Framework** | Pyrogram (MTProto) |
| **Extension** | tgcore (Telegram Core) |
| **Auth Type** | Bot Token / User Session |
| **Handler** | filters.command + filters.me |

## Key Features

- Unified interface for both bot and userbot
- Fluent builders for keyboards and reply parameters
- Type hints for better IDE support
- Clean separation of concerns

## Installation

```bash
pip install tgcore kurigram
```

## Usage Notes

- Remove `filters.me` for bot-only implementation
- Add error handling for production use
- Configure client session appropriately for user/bot mode
