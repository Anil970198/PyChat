from .participant import Participant
from .message import Message

class Room:
    def __init__(self):
        self.participants: dict[str, Participant] = {}
        self.history: list[Message] = []

    def join(self, nickname: str, participant: Participant):
        self.participants[nickname] = participant
        return list(self.history)

    def leave(self, nickname: str):
        if nickname in self.participants:
            del self.participants[nickname]

    def get_nicknames(self):
        return list(self.participants.keys())

    async def broadcast_user_list(self):
        nicknames = ", ".join(self.get_nicknames())
        sys_msg = Message("SYSTEM", f"Users online: {nicknames}")
        for participant in self.participants.values():
            await participant.write(sys_msg)

    async def deliver(self, sender: Participant, message: Message):
        self.history.append(message)
        for participant in self.participants.values():
            if participant != sender:
                await participant.write(message)
