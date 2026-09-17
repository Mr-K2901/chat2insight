def process_text(text: str) -> dict:
    cleaned = " ".join(text.split())
    return {"text": cleaned, "length": len(cleaned)}
