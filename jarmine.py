#MineGrow
#A python minecraft server controller.
#Made by envy#0449
#thx to stackiverflow lol byw haha yes

import shutil
from os.path import join
import os
import time
import sys

print("[+] MineGrow - Minecraft Python Server")
print("[+] Github : whyenvy")
lolwhy = input("[>] Do you wish to start server? (y/n) ")

def server_command(cmd):
    process.stdin.write(cmd+"\n") #just write the command to the input stream
process = None
executable = '"C:\Program Files\Java\jre1.8.0_111\bin\java.exe" -Xms4G -Xmx4G -jar craftbukkit-1.10.2.jar nogui java'
while True:
    command=input()
    command=command.lower()
    if process is not None:
        if command==("start"):
            os.chdir(minecraft_dir)
            process = subprocess.Popen(executable, stdin=subprocess.PIPE)
            print("[+] Server started.")
    else:
        server_command(command)