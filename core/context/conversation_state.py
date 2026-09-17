from dataclasses import dataclass, field


@dataclass
class ConversationState:
    chat_id: str
    message_count: int = 0
    topics: list[str] = field(default_factory=list)
