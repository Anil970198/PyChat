# 💬 PyChat — An Asynchronous Chat Room in Python

**PyChat** is a sleek, vibrant, and fully asynchronous chat room built using Python's `asyncio` and `tkinter`. It enables real-time communication between multiple users with live updates and a modern GUI experience — all without needing a central database or browser.

---

## 🚀 Features

### ✅ Real-Time Asynchronous Messaging
- Uses `asyncio` to support simultaneous reads/writes
- Server can handle many clients concurrently

### 👥 Live User Tracking
- Sidebar shows **currently active users**
- Automatically updates when someone joins or leaves

### 💻 Dual Clients
- **GUI Client** with a stylish `tkinter` interface
- **CLI Client** for terminal lovers

### 🧠 In-Memory Chat History
- New users receive chat history on connect
- Efficient in-memory buffer (no DB needed)

### 🎨 Polished GUI (Tkinter)
- Dark theme with accent colors
- Responsive layout and message input
- Clean button hover effects

---

## 📁 Folder Structure

```
PyChat/
│
├── core/
│   ├── message.py       # Message encoding/decoding logic
│   ├── participant.py   # Abstract base for chat participants
│   ├── room.py          # Manages all active users + broadcasts
│   └── session.py       # Handles per-client session lifecycle
│
├── server.py            # Starts the chat server
├── client.py            # Command-line chat client
├── gui_client.py        # GUI client with sidebar + chat
├── ding.wav             # Optional sound file for notifications
└── README.md
```

---

## 🛠️ How to Run

### 1. Start the Server

```bash
python server.py
```

### 2. Launch GUI Clients (Multiple Windows)

```bash
python gui_client.py
```

Each user can enter a nickname and start chatting.

> 💡 You can also test using `client.py` for CLI-based communication.

---

## 🧪 Tech Stack

- **Python 3.10+**
- `asyncio` for concurrency
- `tkinter` for the GUI
- `simpleaudio` (optional) for sound alerts

---

## 📦 Future Improvements

- [ ] Private Messaging
- [ ] File Transfer Support
- [ ] Emoji Picker 😄
- [ ] Server Authentication / Rooms
- [ ] Deployment as a Desktop `.app`

---

## 📸 Screenshots

> ! [failed to load][working image.png]

---

## 👨‍💻 Author

Built with ❤️ by Anil Kumar  
Inspired by simplicity, powered by Python.

---

## 📝 License

This project is open-source under the [MIT License](LICENSE).

---

Enjoy chatting with PyChat! 🎉