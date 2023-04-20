import os
import webbrowser
import time
def credenziali():
    os.system('figlet Password')
    #inserimento Dati
    print("---------------------->")
    nome = input("inserisci il tuo Username: ")
    print("---------------------->")
    passwd = input("inserisci la password: ")
    os.system('clear')
    #Creazione file
    print(" * ")
    time.sleep(0.6)
    print(" * *  ")
    time.sleep(0.6)
    print(" * * * ")
    time.sleep(0.6)
    print(" * * * * ")
    time.sleep(4)
    f = open("Guida.txt","w")
    f.write("per maggiori info sulla password")
    f.write("\nPassword è koala")
    f.close()
    time.sleep(10)
    os.remove("Guida.txt")
    os.system('clear')
    os.system('figlet arrivederci ' + nome)
credenziali()
