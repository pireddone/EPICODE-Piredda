# Parte 1
def conteggio_lettere(lista_a):
        return[len(parola) for parola in lista_a]
input_utente = input("inserisci le parole separate da spazi: ")
lista_a = input_utente.split()
lista_b = conteggio_lettere(lista_a)
print("Le parole inserite sono: ", lista_a)
print("La lunghezza delle parole inserite è: ", lista_b)
