import sys, time, os


def m(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.1)

os.system("clear")
print("""
      

      ██████╗░░█████╗░████████╗
      ██╔══██╗██╔══██╗╚══██╔══╝
      ██████╦╝██║░░██║░░░██║░░░
      ██╔══██╗██║░░██║░░░██║░░░
      ██████╦╝╚█████╔╝░░░██║░░░
      ╚═════╝░░╚════╝░░░░╚═╝░░░
      ░ ░\x1b[00m\033[041m TERMUX CRONOS BOT 121 \033[00m\x1b[1;00m░░
        ░ ░   ░   ░    ░ ░   ░    ░   ░   ░\x1b[00m
""")
m('\x1b[00m\033[041m Instalação automática de ferramentas  \033[00m')
m('\x1b[00m\033[041m Não saia do Termux antes de terminar de instalar!!  \033[00m')
os.system("pkg update -y")
os.system("pkg upgrade -y")
os.system("pkg install nodejs -y")
os.system("pkg install nodejs-lts -y")
os.system("pkg install ffmpeg -y")
os.system("pkg install wget -y")
os.system("pkg install python2 -y")
os.system("pkg install python3 -y")
os.system("pkg install figlet -y")
os.system("pkg iinstall nano -y")
os.system("pkg install cmatrix -y")
os.system("pkg install git -y")
m('\x1b[00m\033[041m Introdução ao Telegram Bot...  \033[00m')
os.system("clear")
os.system("python start.py")
m("DONE")
