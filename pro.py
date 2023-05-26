import os, sys
try:
    __import__("data").menu()
except Exception as e:
    exit(str(e))
