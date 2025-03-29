import asyncio
from .participant import Participant
from .message import Message

class Session(Participant):
    def __init__(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter, room):
        self.reader = reader
        self.writer = writer
        self.room = room
        self.nickname = "Anonymous"
        self.message_queue = asyncio.Queue()

    async def start(self):
        self.nickname = await self.reader.readline()
        self.nickname = self.nickname.decode().strip() or "Anonymous"
        print(f"[Session] New connection with nickname: {self.nickname}")

        history = self.room.join(self.nickname, self)
        for msg in history:
            await self.write(msg)

        await self.room.broadcast_user_list()

        asyncio.create_task(self.send_messages())
        await self.read_messages()

    async def read_messages(self):
        try:
            while True:
                data = await self.reader.readline()
                if not data:
                    break
                message = Message(self.nickname, data.decode().strip())
                print(f"[Session] Received: {message}")
                await self.deliver(message)
        except asyncio.CancelledError:
            pass
        finally:
            self.room.leave(self.nickname)
            await self.room.broadcast_user_list()
            self.writer.close()
            await self.writer.wait_closed()

    async def deliver(self, message: Message):
        await self.room.deliver(self, message)

    async def write(self, message: Message):
        await self.message_queue.put(message)

    async def send_messages(self):
        while True:
            message = await self.message_queue.get()
            self.writer.write(message.encode())
            await self.writer.drain()

    def __eq__(self, other):
        return isinstance(other, Session) and self.writer == other.writer

    def __hash__(self):
        return hash(id(self.writer))
