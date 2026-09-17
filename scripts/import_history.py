from pathlib import Path

from core.ingestion.export_parser import parse_export


def import_history(path: str) -> int:
    messages = parse_export(path)
    print(f"Imported {len(messages)} messages from {Path(path)}")
    return len(messages)


if __name__ == "__main__":
    import_history("data/exports/chat.txt")
