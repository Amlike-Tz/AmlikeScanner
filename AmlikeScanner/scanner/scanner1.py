#!/usr/bin/python3


#codded by AMLIKETZ

#Colours choosen by amlike
R = '\033[31m' #Red
Y = '\033[93m' #yellow
G = '\033[92m'  #green
clear = '\033[0m'  #clear
B = '\033[1;34m' #Blue
cyan = '\033[96m' #cyan
cy='\033[095m'  #cy

import socket
import os
import time
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)
os.system("clear")
time.sleep(0.5)
os.system("figlet amlike")
print("")
print(R+"\t Developer:@AmlikeTz")
print("")
print(Y+"THIS IS AMLIKE PORT SCANER✓✓ USED TO MAKE ASSURANCE TO THE RESULT OF OPEN PORT YOU GET FROM THE OTHER SCANNER. THIS IS SCANNING SINGLE PORT FOR THE BEST ACCURATE RESULT!!!")
print("")
print("")
host = input("Please enter the IP you want to scan: ")
print("")
time.sleep(0.5)
print(host+B+"::This is an IP to scan✓✓✓")
print("")
port = int(input(G+"[+]Enter Single port to Scan: "))
def amlikeportScaner(port):
    if s.connect_ex((host, port)):
        print("The port is closed")
    else:
        print("The port is open")

amlikeportScaner(port)
