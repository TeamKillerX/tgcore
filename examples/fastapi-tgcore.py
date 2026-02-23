# Optional: https://core.telegram.org/bots/api
# Optional: webhook, support proxy, enterprise-grade
# Learning logic first
# Easy beginner python

from fastapi import FastAPI

from tgcore import Client

app = FastAPI()
tg = Client()

@app.get("/")
def read_root():
    return {"Hello": "Word"}

@app.post("/api/v2/sendMessage")
async def send(chat_id: int, text: str):
    return await tg.raw.sendMessage(
        chat_id=chat_id,
        text=text,
        # add another
    ).execute()

# How to change the Base URL in TGCore
tg.base_url = "https://easy-your-example.com"
