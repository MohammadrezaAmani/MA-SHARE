import asyncio
import os
import pty
import signal
import subprocess
import sys
import threading
import time
import threadpoolctl
from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
from starlette.middleware.cors import CORSMiddleware

app = FastAPI()

# Allow cross-origin requests (for development)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global variables to store the shell process and its output
shell_process = None
output_buffer = []

# Create a pseudo-terminal (pty) and start a shell in it
def start_shell():
    global shell_process, output_buffer
    master, slave = pty.openpty()
    shell = os.environ.get("SHELL", "/bin/bash")
    shell_process = subprocess.Popen(
        [shell],
        stdin=slave,
        stdout=slave,
        stderr=slave,
        preexec_fn=os.setsid,
        universal_newlines=True,
    )
    output_buffer = []

    def capture_output():
        while True:
            output = os.read(master, 1024).decode()
            if output:
                output_buffer.append(output)

    threading.Thread(target=capture_output).start()


# WebSocket endpoint
@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    global shell_process, output_buffer

    try:
        while True:
            data = await websocket.receive_text()
            if data == "exit":
                if shell_process is not None:
                    os.killpg(os.getpgid(shell_process.pid), signal.SIGTERM)
                await websocket.send_text("Exiting terminal...")
                break
            elif data == "clear":
                os.system("clear")
            elif data.startswith("cd "):
                try:
                    os.chdir(data[3:])
                    await websocket.send_text(f"Changed directory to {os.getcwd()}\n")
                except Exception as e:
                    await websocket.send_text(f"Failed to change directory: {str(e)}\n")
            elif data.startswith("sudo "):
                await websocket.send_text("Sudo is not supported in this terminal.\n")
            else:
                if shell_process is None:
                    start_shell()
                if shell_process is not None:
                    # if shell_process.stdin is not None:
                    os.write((data + "\n").encode())
                    # else:
                    #     await websocket.send_text("Shell process stdin is not initialized.\n")
                    time.sleep(0.1)
                    output = "".join(output_buffer)
                    output_buffer = []
                    await websocket.send_text(output)
                else:
                    await websocket.send_text("Shell process is not initialized.\n")
    except Exception as e:
        print(f"WebSocket Error: {e}")
    finally:
        await websocket.close()


@app.get("/", response_class=HTMLResponse)
async def get():
    with open("terminal.html") as f:
        return HTMLResponse(content=f.read())


def run_command(command):
    process = subprocess.Popen(
        command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE
    )
    output, _ = process.communicate()
    return output.decode()


