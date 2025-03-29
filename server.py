import asyncio
from core.session import Session
from core.room import Room

room = Room()

async def handle_client(reader, writer):
    session = Session(reader, writer, room)
    await session.start()

async def main():
    server = await asyncio.start_server(handle_client, "127.0.0.1", 8888)
    addr = server.sockets[0].getsockname()
    print(f"Server running on {addr}")
    async with server:
        await server.serve_forever()

if __name__ == "__main__":
    asyncio.run(main())
