from core.context.context_builder import build_context
from core.context.topic_detector import detect_topics


def process_conversation(messages: list[dict]) -> dict:
    return {
        "context": build_context(messages),
        "topics": detect_topics(messages),
        "message_count": len(messages),
    }
