from core.ingestion.normalizer import normalize_message


def test_normalize_message_cleans_text_and_adds_ingestion_time():
    result = normalize_message({"sender": " Alice ", "text": " hello   world "})
    assert result["sender"] == "Alice"
    assert result["text"] == "hello world"
    assert "ingested_at" in result
