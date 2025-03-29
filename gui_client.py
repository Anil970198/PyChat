import asyncio
import threading
import tkinter as tk
from tkinter import simpledialog, scrolledtext

HOST = '127.0.0.1'
PORT = 8888

class ChatClient:
    def __init__(self, master):
        self.master = master
        self.master.title("💬 Chat Room with Users Online")
        self.master.configure(bg="#1f1f2e")

        self.font = ("Segoe UI", 11)
        self.bg_color = "#1f1f2e"
        self.fg_color = "#ffffff"
        self.input_bg = "#2e2e3e"
        self.accent = "#00bfa6"
        self.hover_bg = "#00c9b1"

        # Chat area
        self.chat_log = scrolledtext.ScrolledText(
            master, bg=self.bg_color, fg=self.fg_color, font=self.font,
            state='disabled', wrap=tk.WORD, borderwidth=0
        )
        self.chat_log.grid(row=0, column=0, columnspan=1, padx=10, pady=10, sticky="nsew")

        # Active user list
        self.user_list = tk.Listbox(
            master, font=self.font, bg="#2b2b3c", fg="#00f7ff",
            borderwidth=0, highlightthickness=0
        )
        self.user_list.grid(row=0, column=1, padx=(0, 10), pady=10, sticky="ns")

        # Message entry
        self.entry = tk.Entry(
            master, bg=self.input_bg, fg=self.fg_color, font=self.font,
            insertbackground=self.fg_color, relief=tk.FLAT,
            highlightthickness=1, highlightbackground=self.accent
        )
        self.entry.grid(row=1, column=0, padx=(10, 0), pady=(0, 10), sticky="nsew")
        self.entry.bind("<Return>", lambda e: self.send_message())

        # Send button
        self.send_button = tk.Button(
            master, text="Send", font=self.font,
            bg=self.accent, fg="#1f1f2e", activebackground=self.hover_bg,
            command=self.send_message, relief=tk.FLAT, cursor="hand2"
        )
        self.send_button.grid(row=1, column=1, padx=(6, 10), pady=(0, 10), sticky="nsew")
        self.send_button.bind("<Enter>", lambda e: self.send_button.config(bg=self.hover_bg))
        self.send_button.bind("<Leave>", lambda e: self.send_button.config(bg=self.accent))

        # Layout config
        master.columnconfigure(0, weight=4)
        master.columnconfigure(1, weight=1)
        master.rowconfigure(0, weight=1)

        self.nickname = simpledialog.askstring("Nickname", "Choose a nickname:", parent=master) or "Anonymous"
        self.reader = None
        self.writer = None

        threading.Thread(target=self.run_event_loop, daemon=True).start()
        self.entry.focus_set()

    def display_message(self, msg):
        self.chat_log.config(state='normal')
        self.chat_log.insert(tk.END, msg + "\n")
        self.chat_log.config(state='disabled')
        self.chat_log.see(tk.END)

        if msg.lower().startswith("system: users online:"):
            users = msg.split(":", 2)[-1].strip().split(", ")
            self.update_user_list(users)

    def update_user_list(self, users):
        self.user_list.delete(0, tk.END)
        for user in users:
            self.user_list.insert(tk.END, f"🟢 {user}")

    def send_message(self):
        msg = self.entry.get().strip()
        if msg and self.writer:
            self.writer.write((msg + "\n").encode())
            asyncio.run_coroutine_threadsafe(self.writer.drain(), self.loop)
            self.entry.delete(0, tk.END)
            self.entry.focus_set()

    async def handle_connection(self):
        self.reader, self.writer = await asyncio.open_connection(HOST, PORT)
        self.writer.write((self.nickname + "\n").encode())
        await self.writer.drain()

        while True:
            data = await self.reader.readline()
            if not data:
                break
            message = data.decode().strip()
            self.master.after(0, self.display_message, message)

    def run_event_loop(self):
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        self.loop.run_until_complete(self.handle_connection())

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatClient(root)
    root.minsize(700, 450)
    root.mainloop()
