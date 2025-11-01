//PRIMA PARTE
//Gioco Epicode quiz

#include <stdio.h> //Serve per input/output
#include <ctype.h> //Maiuscole e minuscole

void introduzione() {
    printf("Benvenuto al Quiz di Epicode\n");
    printf("Rispondi alle domande e diventa Cybersecurity Specialist\n\n");
}

char menu_principale() {
    char selezione;
    printf("Scegli una delle due opzioni: \n");
    printf("A. Inizia un nuovo quiz\n");
    printf("B. Esci dal quiz\n");
    printf("Selezione: ");
    scanf(" %c", &selezione);
    return selezione;
}

int gioco() {
    char nome[30];
    int punti = 0;
    char risposta; //inizializziamo var risposta
    
    //Benvenuto al giocatore
    printf("\n Inserisci il tuo nome: ");
    scanf("%29s", nome);
    printf("\n Benvenuto %s!\n", nome);  //%s = per le stringhe (parole, non numeri, i numeri si richiamano con %d)
    
    //Prima domanda
    printf("\nIn che anno è stata fondata l’Unione Sovietica (URSS)?\n");
    printf("A. 1922 \nB. 1917\nC. 1985\n");
    printf("Risposta: ");
    scanf(" %c", &risposta);
    if(toupper((unsigned char)risposta)== 'A') {
        printf("Risposta Esatta\n");
        punti++;
    } else {
        printf("Risposta errata\n");
        punti--;
    }

    //Seconda domanda
    printf("\nChi fu il primo leader dell’Unione Sovietica?\n");
    printf("A. Lenin \nB. Stalin\nC. Tony da Milano\n");
    printf("Risposta: ");
    scanf(" %c", &risposta);
    if(toupper((unsigned char)risposta)== 'A') {
        printf("Risposta Esatta\n");
        punti++;
    } else {
        printf("Risposta errata\n");
        punti--;
    }

    //Terza domanda
    printf("\nQuale evento segnò la fine dell’Unione Sovietica?\n");
    printf("A. Le dimissioni di Michail Gorbaciov \nB. Parenzo\nC. Lenin Zombie\n");
    printf("Risposta: ");
    scanf(" %c", &risposta);
    if(toupper((unsigned char)risposta)== 'A') {
        printf("Risposta Esatta\n");
        punti++;
    } else {
        printf("Risposta errata\n");
        punti--;
    }

    //Punti Totali
    printf("\n Punti Totali: %d\n", punti);
    return punti;
}

int main() {
    // richiamo variabili, richiamo le funzioni con ()
    char selezione;
    introduzione();
    do {
        selezione = menu_principale();
        switch (toupper(selezione)) {
            case 'A':
                gioco();
                break;
            case 'B':
                printf("Arrivederci \n");
                break;
            default: 
                printf("Scelta non valida\n");
                break;
        }
        //se la scelta è diversa da B continua la routine
    } while(toupper(selezione) != 'B');
    return 0;

}

// La prima parte dell'esercizio non funzionava, con l'aiuto di codex ho scoperto
// che il problema erano gli spazi, poichè scrivevo ("%c") e invece andava scritto (" %C"),
// in più per evitare problemi mi ha consigliato di aggiungere  unsigned char al toupper.

//PARTE FACOLTATIVA

int main() {
    char scelta;
    int punteggio_totale = 0; //azzeriamo la variabile

    presentazione();

    do {
        scelta = menu_principale() //assegnamo alla variabile la funzione
        switch(toupper(scelta)) {
            case 'A':
                punteggio_totale += gioco();
                printf("Punteggio totale: %d\n", punteggio_totale);
                break;
            case 'B':
                printf("Punteggio totale: %d\n", punteggio_totale);
                printf("Alla prossima\n");
            default:
                printf("Scelta non valida\n");
                break;
        }
    } while(toupper(scelta) != 'B');
    return 0;
}
