import os, sys
try:import httpx
except:os.system('pip install httpx > /dev/null')
os.system('git pull')
try:
    __import__("ab").main()
except Exception as e:
    exit(str(e))
