
#!user/bin/python
import requests, json
import os
import sys
import datetime
import time
#Colours choosen by amlike
#Colours choosen by amlike
R = '\033[31m' #Red
Y = '\033[93m' #yellow
G = '\033[92m'  #green
clear = '\033[0m'  #clear
B = '\033[1;34m' #Blue
cyan = '\033[96m' #cyan
cy='\033[095m'  #cy
cya='\033[035m' #cya
red = '\033[31m'
yellow = '\033[93m'
green = '\033[92m'
clear = '\033[0m'
bold = '\033[01m'
cyan = '\033[96m'
cy='\033[095m'
cya='\033[035m'
os.system("clear")
os.system("figlet AmlikeTz")
import datetime
x = datetime.datetime.now()
time.sleep(2)
print(x.strftime("%d-%m-%Y"))
time.sleep(1)
print(yellow +"\t\t  _author_ @mlikeTz!!")
time.sleep(2)
print("\t\t\t\tv 1.0.0")
print("")
os.system("")
time.sleep(1)
os.system("figlet amliketz")
print("")
time.sleep(1)
print(red+bold+"THIS TOOL IS ONLY FOR EDUCATIONAL PURPOSES ONLY. AMLIKE OR TEAM AMLIKETZ THEY WILL NOT BE RESPONSIBLE FOR ANY MISUSE")
print("")
Y=input("Agree to continue>>>press 'Y' to continue 'N' to exit the tool: ")
time.sleep(0.5)
print("")
print("")
name=input(yellow +" What is your name:  ")
time.sleep(1)
print("")
print("")
print(name +red+"  >>Welcome to amlike scanner tool this tool is free of charge but if ur loyality you may support Amlike project by giving him some donation™✓✓ ®™✓✓Support young Tanzanian Developer")
print("")
time.sleep(1)
print("")
print("")
print("please wait..Fetching data[*][*]")
time.sleep(20)
os.system("clear")
print("")
print("")
print(B+"SORRY FOR INCONVINIENCE THIS TOOL IS NOT YET COMPLETED ONLY ONE SEGEMENT WORKFINE. FOR ANY BUGS CONTACT DEVELOPER AND KEEP UPDATING THE TOOL SO WIIL BE FIXED AFTER DEVELOPER MAKE AN UPDATE ON THIS")
time.sleep(10)
os.system("clear")
time.sleep(1)
print(red+"******†††††††*†*****coded by AmlikeTz cyber killer")
os.system("clear")
print("")
time.sleep(2)
os.system("clear")
time.sleep(1)
os.system("cd new;cd banner;python banner1.py")
print("\t Suport Tanzanian Developers™✓✓") 
x = datetime.datetime.now()
print(x.strftime("\t  %d-%m-%Y"))
print("")
time.sleep(1)
print("1:- AmlikeTz IP Scanner")
print("")
print(R+"2:- AmlikeTz Web Scanner")
print("")
print(cya+"3:- Amlike Viruses")
print("")
print(yellow+"4:- UPDATE Team AmlikeTz Tool")
print("")
print(B+"0:- BACK TO MAIN MENU")
print("")
time.sleep(1)
for i in range (100):
       com=input(G+"Enter your choice: ")
       if com=="1":
                os.system("clear")
                time.sleep(3)
                os.system("figlet FIND IP")
                print(B+"\t\t  Coded by: Amlike")
                print("")
                print("")
                ip=input(green+bold+"[*] Enter Victim Ip:  ")
                response ="http://ip-api.com/json/"
                re=requests.get(response+ip).json()
                print("")
                print("")
                print(yellow+bold+"##############TAARIFA ZA VICTIM WAZO#############")
                print(red+"[ * ] Victim ip:~~~~~~",re["query"])
                print("")
                print(cyan+"[ * ] Status Code:++++++",re["status"])
                print("")
                time.sleep(0.5)
                print(cy+"[ * ] Victim Country:=====",re["country"])
                print("")
                time.sleep(0.5)
                print(cya+"[ * ] Victim Country Code:::::::",re['countryCode'])
                print("")
                time.sleep(0.5)
                print(cyan+"[ * ] Victim Region:-----",re["region"])
                print("")
                time.sleep(0.5)
                print(green+"[ * ] Victim RegionName:******",re["regionName"])
                print("")
                time.sleep(0.5)
                print(cy+"[ * ] Victim City:$$$$$$",re["city"])
                print("")
                time.sleep(0.5)
                print(green+"[ * ] Latitude:>>>>>",re["lat"])
                print("")
                time.sleep(0.5)
                print(cy+"[ * ] Longitude:......",re["lon"])
                print("")
                time.sleep(0.5)
                print(red+"[ * ] Victim TimeZone:,,,,,,",re["timezone"])
                print("")
                time.sleep(0.5)
                print(cyan+"[ * ] Victim Isp:<=====>",re["isp"])
                print("")
                time.sleep(0.5)
                print(cy+"[ * ] Victim Org:xxxxxx",re["org"])
                print("")
                time.sleep(0.5)
                print(cya+"[ * ] Victim As:888888",re["as"])
                print("")
                print("")
                time.sleep(0.5)
                print("")
                print("")
                print("")
                print(B+"Support Amlike project by giving him some dination of money inorder to make him fell suported. proud for your local developer")
       if com=="2":
                os.system("clear")
                time.sleep(1)
                print("")
                os.system("figlet WEB")
                print("")
                print(R+"\t  Developer: AmlikeTz")
                print("")
                print("")
                print("[1]: Scan Real single Open port")
                print("")
                print("[2]: Nmap All Port")
                print("")
                for i in range (50):
                      dr=input(G+"[*]Enter your choice: ")
                      if dr=="1":
                              os.system("clear")
                              os.system("figlet PORT")
                              print("")
                              print(R+"\t  Developer:AMLIKE™✓✓")
                              print("")           
                              os.system("cd new;cd scanner;python scanner1.py")
       if com=="3":
                os.system("clear")
                time.sleep(1)
                os.system("cd new;cd virus;python virus1.py")
       if com=="4":
                os.system("clear")
                os.system("figlet Upgrading amlike scanner")
                os.system("cd /data/data/com.termux/files/home")
                os.system("pkg install python")
                os.system("pkg install git")
                os.system("pkg install lolcat")
                os.system("cd;rm -rf AmlikeScanner;https://github.com/Amlike-Tz/AmlikeScanner.git")
                os.system(yellow+"\t UPGRADING COMPLETED NOW THE TOOL IS UP TO DATE.ENJOY")
                time.sleep(2)
                os.system("cd AmlikeScanner;python AmlikeScanner.py")
                print("")
       if com=="0":
                os.system("clear")
                print("")

                print("")
                print("PLEASE WAIT...&& BACK TO MAIN MENU")
                time.sleep(3)
                os.system("/data/data/com.termux/files/home && cd AmlikeScanner")
                os.system("python AmlikeScanner.py")
#       else: 
                os.system("clear")
                print("")
                print("")
                print("CHAGUO SIO SAHIHI.TOOL IS EXITING")
                sys.exit
