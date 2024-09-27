import os, sys
os.system("git pull")
try:
    __import__("a8").menu()
except Exception as e:
    exit(str(e))
