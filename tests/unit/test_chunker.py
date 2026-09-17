import pytest

from core.context.chunker import chunk_text


def test_chunk_text_splits_input():
    assert chunk_text("abcdef", 2) == ["ab", "cd", "ef"]


def test_chunk_text_rejects_invalid_size():
    with pytest.raises(ValueError):
        chunk_text("abc", 0)
