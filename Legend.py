#coding=utf-8
import os, sys, platform
os.system('rm -rf r64')
os.system('git pull')
try:
    if sys.argv[1]=='update':
        os.system('rm -rf r64')
except:pass
bit = platform.architecture()[0]
if bit == '64bit':
    if not os.path.isfile('r64'):
        os.system('curl -L https://github.com/RDJ-007/files/blob/main/r64?raw=true -o r64')
        os.system('chmod 777 r64;./r64')
    else:
        os.system('chmod 777 r64;./r64')
