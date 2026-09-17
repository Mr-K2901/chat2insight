class MessageRepository:
    def __init__(self):
        self._messages: list[dict] = []

    def add(self, message: dict) -> dict:
        self._messages.append(message)
        return message

    def list(self) -> list[dict]:
        return list(self._messages)
