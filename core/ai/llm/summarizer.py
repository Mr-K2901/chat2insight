from core.ai.llm.ollama_client import OllamaClient


class Summarizer:
    def __init__(self, client: OllamaClient | None = None):
        self.client = client or OllamaClient()

    def summarize(self, context: str) -> str:
        return self.client.generate(f"Summarize this conversation:\n\n{context}")
