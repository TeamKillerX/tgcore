## Why fluent builder?

Traditional Telegram API calls often require many parameters.

This leads to what developers call **"parameter hell"**.

![brain meme](https://cdn.ryzenths.dpdns.org/amlve3.jpg)

```py
send_message(
 chat_id,
 text,
 parse_mode,
 disable_notification,
 reply_markup,
 protect_content,
 ...
)
```

![brain meme](https://cdn.ryzenths.dpdns.org/IMG_20260315_003008_575.jpg)

Instead of passing many parameters at once,
TGCore uses a fluent builder interface.

`tg.send().chat_id().text().send()`

## Telegram API
```py
send_message(chat_id, text, parse_mode, disable_notification...)
```

## TGCore

`tg.send().chat_id().text().send()`

# Level architecture

TGCore is not just a library.
It's an SDK architecture.

Full documentation is available in [the docs](https://tgcore.ryzenths.dpdns.org/api/v2/docs).

Without explanation, the architecture may look confusing. ⊙⁠﹏⁠⊙

![brain meme](https://cdn.ryzenths.dpdns.org/IMG_20260315_005158_516.jpg)

## Quick start example

TGCore is an asynchronous Telegram SDK framework for Python
designed around a fluent builder architecture.

It eliminates parameter-heavy API calls and replaces them with
a composable chain-based interface.

```bash
pip install tgcore
```

Create a client and send your first message:
```py
from tgcore import Client

tg = Client(api_key="YOUR_API_KEY")

await tg.raw.sendMessage()\
    .chat_id(123456789)\
    .text("Hello from TGCore")\
    .send()
```

![brain meme](https://cdn.ryzenths.dpdns.org/IMG_20260315_010120_852.jpg)

An example of keyboard or reply markup will demonstrate the power of chaining:
```py
kb = tg.kb().copy_text("Click", "ok").build()

await tg.raw.sendMessage()\
    .chat_id(123456789)\
    .text("Hello")\
    .reply_markup(kb)\
    .send()
```

## List Methods
- `tg.api_key`
- `tg.base_url`

```py
tg._ensure_client().get(url, params, json, headers)
tg._ensure_client().post(url, params, json, headers)

tg._headers(extra={})
tg.set_header(key, value)
tg.to_obj(data)
tg.kb() # KeyboardBuilder
tg.lw() # LinkPreviewBuilder
tg.rs() # ReplyParametersBuilder
tg.is_url(text)

tg.writer(prefix, cbytes, is_base64=False)

tg._post(
   path="/api/todo",
   payload={},
   headers={},
   is_content=False
)

tg._get(
   path="/api/todo",
   payload={},
   headers={},
   is_content=False
)

tg.fetch_post(path, **kw)
```

## RequestCall
```py
tg.use.default.types().step().execute()

tg.use.default.types().step().skip()

tg.use.default.types().step().send(allow_object=False, via_result=False)

tg.use.default.types().step().pretty()

```

## Platform
parameters
* `url`
* tg.platform.`<method>`

```py
user = await tg.platform.facebook\
       .download()\
       .url()\
       .send(via_result=True)\

return user.video_url(0)
```

parameters
* `pinUrl`

```py
user = await tg.platform.pinterest\
       .download()
       .pinUrl("https://pinterest.com/pin/914862421155199/")
       .send(via_result=True)

return user.pins_urls()
```

parameters
* `platform`
* `url`

```py
user = await tg.platform.tools\
       .types()
       .platform("instagram")
       .url("")
       .send()

return user
```

## Blackforest
parameters
* `query`

```py
user = await tg.platform.blackforest\
      .image()\
      .query("HERE")\
      .send(via_result=True)\

return user.image_bytes()
```

## chatCompletions
parameters
* `model`
* `messages`
* `stream`

```py
resp = await tg.raw.chatCompletions()\
    .model("kimi-dev")\
    .messages(
      [{"role": "user", "content": "say test"}]
    )\
    .stream(False)\
    .send(via_result=True)\

return resp.text()
```

## How to Automatically Save base_url?

You can set `base_url` when using the userbot:

1. **During initialization:**
`tg = Client(base_url="https://tgcore.ryzenths.dpdns.org")`
3. Or by assigning it directly:
`tg.base_url = "https://tgcore.ryzenths.dpdns.org"`

This value will be saved and will persist.

Code Example:
```py
MEME_IG_URL = "https://www.instagram.com/reel/......"

result = await tg.use.default\
    .types("/api/web/platform/download")\
    .platform("instagram")\
    .url(MEME_IG_URL)\
    .send(allow_object=True)

return result
```

## JSON vs Fluent Builder: Key Differences

**JSON Approach:**
- Data is structured as a dictionary/object
- Static structure defined upfront
- Less flexible for conditional logic
- Example: `{"step": "this", "step2": "value"}`

**Fluent Builder Approach:**
- Chainable methods for dynamic construction
- More readable and expressive
- Easier to implement conditional steps
- Better IDE autocomplete support

**Your Example:**
```python
# JSON style
data = {"step": "this"}

# Fluent Builder style
result = await tg.use.default\
    .types("/api/todo")\
    .step()\
    .step2()\
    .step3()\
    .send()
```

**Key Advantage:** Fluent builder allows dynamic step-by-step construction while maintaining readability.

## Is TgCore Free?

Yes, it's completely free with the following limits:

- **Access:** Bot, platform, and AI features
- **Trial Period:** 7-day validity
- **API Key Types:**
  - `fw_trial_xxx` = 7-day validity
  - `fw_live_xxx` = valid for 30 days (renewable)
