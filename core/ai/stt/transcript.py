from dataclasses import dataclass


@dataclass
class Transcript:
    text: str
    language: str | None = None
    confidence: float | None = None
