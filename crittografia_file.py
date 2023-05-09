import os
def crittografia():
    while True:
        os.system('clear')
        os.system('figlet Crittografia')
        password = "sasso"
        passwd = input("\nenter password --------> ")
        if passwd == password:
            os.system('clear')
            os.system('python3 password.py')
            exit()
        else:
            os.system('clear')
            print("Password errata")
crittografia()
