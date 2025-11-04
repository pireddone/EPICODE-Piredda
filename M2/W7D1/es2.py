# Parte 2 (password generator)
import random
import string

def scegli_psw():
    print("Genera Password")
    complessa = string.digits + string.ascii_letters + string.punctuation
    semplice = string.digits + string.ascii_letters
    if input("Semplice o Complessa? S/C ") == "C":
        lunghezza = 20
        tipo = complessa
    else:
        lunghezza = 8
        tipo = semplice
    
    password = ""
    counter = 0

    while counter < lunghezza:
        char = random.choice(tipo)
        password += char
        counter += 1
    print(f"La tua password è: {password}")

scegli_psw()