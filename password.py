import os
import webbrowser
def credenziali():
    #inserimento Dati
    print("---------------------->")
    nome = input("inserisci il tuo Username: ")
    print("---------------------->")
    passwd = input("inserisci la password: ")
    os.system('clear')
    #Creazione file
    f = open("credenziali.txt","w")
    f.write("username " + nome)
    f.write("\npassword " + passwd)
    f.close()
credenziali()
def verifica_passwd():
    print("digita Y/n")
    scelta = input("vuoi verificare che la tua passwd sia forte: ")
    if scelta == 'Y':
        w = webbrowser.open('https://password.kaspersky.com/it/')
    else:
        print("allora ok")
    os.remove("credenziali.txt")
    os.system('clear')
verifica_passwd()