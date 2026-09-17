from core.processors.text_processor import process_text


def route_media(message: dict) -> dict:
    media_type = message.get("media_type", "text")
    if media_type == "text":
        return process_text(message.get("text", ""))
    return {"media_type": media_type, "status": "queued"}
