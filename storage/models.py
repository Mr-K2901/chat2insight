from dataclasses import dataclass
from datetime import datetime


@dataclass
class Message:
    chat_id: str
    sender: str
    text: str
    timestamp: datetime | None = None
