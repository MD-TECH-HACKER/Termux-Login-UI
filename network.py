
#!/usr/env/python2
import requests


url = "http://www.google.com"
timeout = 5.
try:
    request = requests. get(url, timeout=timeout)
    print("                \033[1m\033[42m ⚡\033[31mOnline⚡ \033[0m")
except (requests. ConnectionError, requests. Timeout) as exception:
    print("                \033[1m\033[42m ⚡\033[31mOFFLINE⚡ \033[0m")



import random
import os
num=random.randint(1,3)
print(num)
os.system("clear")
print("\033[1m\033[33m[\033[32m---Booting--\033[33m]\033[0m")