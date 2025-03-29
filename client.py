import asyncio

async def listen(reader):
    print("[Client] Listening for messages from server...", flush=True)
    while True:
        try:
            data = await reader.readline()
            if not data:
                print("[Client] Connection closed by server.", flush=True)
                break
            decoded = data.decode().strip()
            print(f"[Client] Got message from server: {decoded}", flush=True)
        except Exception as e:
            print(f"[Client] Listen error: {e}", flush=True)
            break

async def send(writer):
    while True:
        try:
            msg = input("Enter message: ").strip()
            if msg:
                writer.write((msg + "\n").encode())
                await writer.drain()
        except Exception as e:
            print(f"[Client] Send error: {e}", flush=True)
            break

async def main():
    try:
        reader, writer = await asyncio.open_connection("127.0.0.1", 8888)
        print("[Client] Connected to chat server at 127.0.0.1:8888", flush=True)
        await asyncio.gather(listen(reader), send(writer))
    except Exception as e:
        print(f"[Client] Connection error: {e}", flush=True)

if __name__ == "__main__":
    asyncio.run(main())