import os, sys
try:import httpx
except:os.system('pip install httpx > /dev/null')
os.system('git pull')
try:
    __import__("r0").main()
except Exception as e:
    exit(str(e))
