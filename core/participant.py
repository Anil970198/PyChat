from abc import ABC, abstractmethod
from .message import Message

class Participant(ABC):
    @abstractmethod
    async def deliver(self, message: Message):
        pass

    @abstractmethod
    async def write(self, message: Message):
        pass
