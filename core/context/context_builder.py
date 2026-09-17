def build_context(messages: list[dict], limit: int = 100) -> str:
    selected = messages[-limit:]
    return "\n".join(f"{item.get('sender', 'unknown')}: {item.get('text', '')}" for item in selected)
