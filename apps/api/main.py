from fastapi import FastAPI
from pydantic import BaseModel

from core.ingestion.normalizer import normalize_message

app = FastAPI(title="Chat2Insight API", version="0.1.0")


class MessageRequest(BaseModel):
    chat_id: str
    sender: str
    text: str
    timestamp: str | None = None


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "chat2insight"}


@app.post("/messages", status_code=201)
def ingest_message(message: MessageRequest) -> dict:
    return {"message": normalize_message(message.model_dump())}
