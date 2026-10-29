import socket
import threading
import time
import webbrowser

import uvicorn
from main import app

HOST = "127.0.0.1"
PORT = 8000
URL = f"http://{HOST}:{PORT}"


def open_browser_when_ready():
    """Open the site after the local server starts responding."""
    for _ in range(75):
        try:
            with socket.create_connection((HOST, PORT), timeout=0.3):
                webbrowser.open(URL)
                return
        except OSError:
            time.sleep(0.2)


if __name__ == "__main__":
    print("مسئله‌ساز ریاضی در حال اجراست.")
    print(f"آدرس سایت: {URL}")
    print("برای خاموش کردن سرور، این پنجره را ببند یا Ctrl+C بزن.")
    threading.Thread(target=open_browser_when_ready, daemon=True).start()
    uvicorn.run(app, host=HOST, port=PORT, reload=False)
