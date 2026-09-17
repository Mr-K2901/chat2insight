from core.pipeline.pipeline import process_conversation


def route(messages: list[dict]) -> dict:
    return process_conversation(messages)
