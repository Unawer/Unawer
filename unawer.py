import sys
import os, time

if os.getuid() != 0:
	print("Este script requiere de privilegios de root (sudo)")	
	sys.exit()
os.system("clear")

def banner():
	print("""
          _        _______           _______  _______   _________ _______ 
|\     /|( (    /|(  ___  )|\     /|(  ____ \(  ____ )  \__   __/(  ____ \
| )   ( ||  \  ( || (   ) || )   ( || (    \/| (    )|     ) (   | (    \/
| |   | ||   \ | || (___) || | _ | || (__    | (____)|     | |   | (__    
| |   | || (\ \) ||  ___  || |( )| ||  __)   |     __)     | |   |  __)   
| |   | || | \   || (   ) || || || || (      | (\ (        | |   | (      
| (___) || )  \  || )   ( || () () || (____/\| ) \ \__     | |   | (____/\
(_______)|/    )_)|/     \|(_______)(_______/|/   \__/     )_(   (_______/
                                                                          
 _______           _        _______ 
(  ____ \|\     /|( (    /|(  ___  )
| (    \/| )   ( ||  \  ( || (   ) |
| (__    | |   | ||   \ | || (___) |
|  __)   | |   | || (\ \) ||  ___  |
| (      | |   | || | \   || (   ) |
| )      | (___) || )  \  || )   ( |
|/       (_______)|/    )_)|/     \|
")

X = input("\033[1;44;37mElige una herramienta:\033[0;m \033[1;36m\n\n>\033[0;m ")

if X == "1":
    tool = os.system("apt-get install nmap")
elif X == "2":
    tool = os.system("apt-get install nikto -y")
elif X == "3":
    tool = os.system("apt-get install john")
elif X == "4":
    tool = os.system("apt-get install wifite")
elif X == "5":
    tool = os.system("apt-get install metasploit-framework")
elif X == "6":
    tool = os.system("apt-get install sqlmap")
elif X == "7":
    tool = os.system("apt-get install aircrack-ng")
elif X == "8":
    tool = os.system("apt-get install hashcat")
elif X == "9":
    tool = os.system("apt-get install legion -y")
elif X == "10":
    tool = os.system("apt-get install wpscan")
elif X == "11":
    tool = os.system("apt-get install wireshark")
elif X == "12":
    tool = os.system("apt-get install crunch -y")
elif X == "13":
    tool = os.system("apt-get install cewl")
elif X == "14":
    tool = os.system("apt-get install medusa")
elif X == "15":
    tool = os.system("apt-get install reaver")
elif X == "16":
    tool = os.system("apt-get install ncrack")
elif X == "17":
    tool = os.system("apt-get install hydra-gtk")
elif X == "18":
    tool = os.system("apt-get install ettercap")
    tool = os.system("apt-get install ettercap-graphical")
elif X == "19":
    tool = os.system("apt-get install macchanger -y")
elif X == "20":
    tool = os.system("apt-get install dnschef")
elif X == "21":
    tool = os.system("apt-get install autopsy")
elif X == "22":
    tool = os.system("apt-get install pipal")
elif X == "23":
    tool = os.system("apt-get --assume-yes install git make gcc")
    tool = os.system("git clone https://github.com/robertdavidgraham/masscan")
    tool = os.system("cd masscan")
    tool = os.system("make install")
elif X == "24":
    tool = os.system("apt-get install whatweb -y")
elif X == "25":
    tool = os.system("apt-get install maltego-teeth")
elif X == "26":
    tool = os.system("apt-get install armitage")
elif X == "27":
    tool = os.system("apt-get install arping")
elif X == "28":
    tool = os.system("apt-get install proxychains -y")
elif X == "29":
    tool = os.system("apt-get install tor torbrowser-launcher")
elif X == "0":
    tool = os.system("exit")
    time.sleep(1)
