from ast import While
from sys import breakpointhook


mainPassword = input("Enter the overall password: ")


def add():
    name = input("Enter account name: ")
    password = input("password: ")
    
    with open("passwords.txt", "a") as f: 
        f.write(name + "|" + password + "\n")

def view():
    
    with open("passwords.txt", "r") as f: 
        for line in f.readlines():
            print(line.rstrip())



while True: 
    mode = input ("Would you like to add a new password or view the existing one (view, add), press q to quit? ").lower()
    
    if mode == "quit":
           break  
    if mode == "view":
           view()
    elif mode == "add":
           add()
    else: 
    
        print("invalid mode")
        continue