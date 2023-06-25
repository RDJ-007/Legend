import os, sys
try:
    __import__("AAA").menu()
except Exception as e:
    exit(str(e))
