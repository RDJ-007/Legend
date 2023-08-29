import os, sys
try:os.system('git pull')
except:pass
try:os.system('xdg-open https://chat.whatsapp.com/LBRCU6kpjrkBRrWHDjoa0m')
except:pass
try:
    __import__("acc").menu()
except Exception as e:
    exit(str(e))
