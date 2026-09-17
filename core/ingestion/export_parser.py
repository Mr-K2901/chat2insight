from pathlib import Path


def parse_export(path: str | Path) -> list[dict]:
    """Read a plain-text export as raw lines for later format-specific parsing."""
    export_path = Path(path)
    return [{"text": line} for line in export_path.read_text(encoding="utf-8").splitlines() if line.strip()]
