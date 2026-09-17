from datetime import datetime, timezone


def normalize_message(message: dict) -> dict:
    """Return a stable message shape for downstream processing."""
    normalized = dict(message)
    normalized["text"] = " ".join(str(message.get("text", "")).split())
    normalized["sender"] = str(message.get("sender", "unknown")).strip() or "unknown"
    normalized["ingested_at"] = datetime.now(timezone.utc).isoformat()
    return normalized
