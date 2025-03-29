class Message:
    def __init__(self, sender: str, content: str):
        self.sender = sender
        self.body = content.strip()

    def encode(self) -> bytes:
        return f"{self.sender}:{self.body}\n".encode()

    @classmethod
    def decode(cls, data: bytes) -> "Message":
        text = data.decode().strip()
        if ':' in text:
            sender, body = text.split(":", 1)
        else:
            sender, body = "Unknown", text
        return cls(sender, body)

    def __str__(self):
        return f"{self.sender}:{self.body}"
