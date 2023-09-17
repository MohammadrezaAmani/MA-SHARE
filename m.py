# i want to write command is terminal using os and shutil modules
import os
import shutil
import subprocess
import sys
import threading
import time
import threadpoolctl

# get a command from input() and run it in terminal and print output using thread

def run_command(command):
    "run command in terminal"
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    while True:
        output = process.stdout.readline().decode()
        if output == '' and process.poll() is not None:
            break
        if output:
            print('out '+output.strip())
    rc = process.poll()
    return rc

def main():
    "main function"
    threadpool = threadpoolctl.threadpool_limits(limits=1, user_api=None)
    with threadpool:
        while True:
            command = input(">>> ")
            if command == "exit":
                sys.exit()
            elif command == "clear":
                os.system("clear")
            
            else:
                thread = threading.Thread(target=run_command, args=(command,))
                thread.start()
                thread.join()
                time.sleep(0.1)

main()