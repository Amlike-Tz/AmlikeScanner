#Colours choosen by amlike
R = '\033[31m' #Red
Y = '\033[93m' #yellow
G = '\033[92m'  #green
clear = '\033[0m'  #clear
B = '\033[1;34m' #Blue
cyan = '\033[96m' #cyan
cy='\033[095m'  #cy
cya='\033[035m' #cya

import time
import os
import sys
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.01)
os.system("clear")
time.sleep(0.5)
delay_print(R+"#######################################")
time.sleep(0.1)
delay_print(R+"#                                     #")
time.sleep(0.1)
delay_print(Y+"#\tAuthor√√:All Team AmlikeTz M  #")
time.sleep(0.1)
delay_print(Y+"#                                     #")
delay_print(G+"#\tChat me on Telegram: @AmlikeTz#")
time.sleep(0.1)
delay_print(G+"#                                     #")
delay_print(B+"#\tCoded by: AmlikeTz            #")
time.sleep(0.1)
delay_print(cy+"#######################################")
time.sleep(0.1)

