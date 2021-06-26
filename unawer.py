import sys
import os, time

if os.getuid() != 0:
	print("Este script requiere de privilegios de root (sudo)")	
	sys.exit()
os.system("import sys")
import os, time

if os.getuid() != 0:
	print("\033[1;31m\nError:\033[0;m Este script requiere de privilegios de root (sudo)")
	sys.exit()

os.system("clear")

def banner():
	print("""
opy & paste this ascii graphic and use it e.g. as mail signature	
          _        _______           _______  _______ 
|\     /|( (    /|(  ___  )|\     /|(  ____ \(  ____ )
| )   ( ||  \  ( || (   ) || )   ( || (    \/| (    )|
| |   | ||   \ | || (___) || | _ | || (__    | (____)|
| |   | || (\ \) ||  ___  || |( )| ||  __)   |     __)
| |   | || | \   || (   ) || || || || (      | (\ (   
| (___) || )  \  || )   ( || () () || (____/\| ) \ \__
(_______)|/    )_)|/     \|(_______)(_______/|/   \__/
Noob hacking for iSH""")
banner()


def menu():
	print("""
\033[1;37m(1)\033[0;m \033[0;32mNmap\033[0;m               \033[1;37m(11)\033[0;m \033[0;32mWireshark\033[0;m     \033[1;37m(21)\033[0;m \033[0;32mAutopsy\033[0;m
\033[1;37m(2)\033[0;m \033[0;32mNikto\033[0;m              \033[1;37m(12)\033[0;m \033[0;32mCrunch\033[0;m        \033[1;37m(22)\033[0;m \033[0;32mPipal\033[0;m
\033[1;37m(3)\033[0;m \033[0;32mJohn the Ripper\033[0;m    \033[1;37m(13)\033[0;m \033[0;32mCewl\033[0;m          \033[1;37m(23)\033[0;m \033[0;32mMasscan\033[0;m
\033[1;37m(4)\033[0;m \033[0;32mWifite\033[0;m             \033[1;37m(14)\033[0;m \033[0;32mMedusa\033[0;m        \033[1;37m(24)\033[0;m \033[0;32mWhatWeb\033[0;m
\033[1;37m(5)\033[0;m \033[0;32mMetasploit\033[0;m         \033[1;37m(15)\033[0;m \033[0;32mReaver\033[0;m        \033[1;37m(25)\033[0;m \033[0;32mMaltego\033[0;m
\033[1;37m(6)\033[0;m \033[0;32mSqlmap\033[0;m             \033[1;37m(16)\033[0;m \033[0;32mNcrack\033[0;m        \033[1;37m(26)\033[0;m \033[0;32mArmitage\033[0;m
\033[1;37m(7)\033[0;m \033[0;32mAircrack-ng\033[0;m        \033[1;37m(17)\033[0;m \033[0;32mHydra\033[0;m         \033[1;37m(27)\033[0;m \033[0;32mArping\033[0;m
\033[1;37m(8)\033[0;m \033[0;32mHashCat\033[0;m            \033[1;37m(18)\033[0;m \033[0;32mEtterCap\033[0;m      \033[1;37m(28)\033[0;m \033[0;32mProxyChains\033[0;m
\033[1;37m(9)\033[0;m \033[0;32mLegion\033[0;m             \033[1;37m(19)\033[0;m \033[0;32mMACchanger\033[0;m    \033[1;37m(29)\033[0;m \033[0;32mTor-Browser\033[0;m
\033[1;37m(10)\033[0;m \033[0;32mWPScan\033[0;m            \033[1;37m(20)\033[0;m \033[0;32mDNSchef\033[0;m       \033[1;37m(0)\033[0;m \033[0;31mSalir\033[0;m\033[0;37m/\033[0;m\033[0;31mExit\033[0;m
""")
menu()

X = input("\255[1;44;37mElige una herramienta:\033[0;m \033[1;36m\n\n>\033[0;m ")

if X == "1":
    tool = os.system("apk add nmap")
elif X == "2":
    tool = os.system("apk add nikto -y")
elif X == "3":
    tool = os.system("apk add john")
elif X == "4":
    tool = os.system("apk add wifite")
elif X == "5":
    tool = os.system("apk add metasploit-framework")
elif X == "6":
    tool = os.system("apk add sqlmap")
elif X == "7":
    tool = os.system("apk add aircrack-ng")
elif X == "8":
    tool = os.system("apk add hashcat")
elif X == "9":
    tool = os.system("apk add legion -y")
elif X == "10":
    tool = os.system("apk add wpscan")
elif X == "11":
    tool = os.system("apk add wireshark")
elif X == "12":
    tool = os.system("apk add crunch -y")
elif X == "13":
    tool = os.system("apk add cewl")
elif X == "14":
    tool = os.system("apk add medusa")
elif X == "15":
    tool = os.system("apk add reaver")
elif X == "16":
    tool = os.system("apk add ncrack")
elif X == "17":
    tool = os.system("apk add hydra-gtk")
elif X == "18":
    tool = os.system("apk add ettercap")
    tool = os.system("apk add ettercap-graphical")
elif X == "19":
    tool = os.system("apk add macchanger -y")
elif X == "20":
    tool = os.system("apk add dnschef")
elif X == "21":
    tool = os.system("apk add autopsy")
elif X == "22":
    tool = os.system("apk add pipal")
elif X == "23":
    tool = os.system("apk add git make gcc")
    tool = os.system("git clone https://github.com/robertdavidgraham/masscan")
    tool = os.system("cd masscan")
    tool = os.system("make install")
elif X == "24":
    tool = os.system("apk add whatweb -y")
elif X == "25":
    tool = os.system("apk add maltego-teeth")
elif X == "26":
    tool = os.system("apk add armitage")
elif X == "27":
    tool = os.system("apk add arping")
elif X == "28":
    tool = os.system("apk add proxychains -y")
elif X == "29":
    tool = os.system("apk add tor torbrowser-launcher")
elif X == "0":
    tool = os.system("exit")
    time.sleep(1)
    print("\n\033[1;32mGracias por usar este script, vuelve nuevamente\033[0;m\033[1;37m!\033[0;m")
else:
    print("\033[1;31m\nError:\033[0;m Carácter incorrecto, intente de nuevo")
