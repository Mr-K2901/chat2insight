from core.ingestion.normalizer import normalize_message


def parse_messages(messages: list[dict]) -> list[dict]:
    return [normalize_message(message) for message in messages]
