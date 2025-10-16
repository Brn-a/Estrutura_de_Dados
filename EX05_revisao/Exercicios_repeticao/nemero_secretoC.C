#include <stdio.h>
#include <stdlib.h> 
#include <time.h>   

int main() {
  
    srand(time(0)); 

    int numero_secreto = (rand() % 100) + 1;
    int palpite = 0;

    printf("--- JOGO: ADIVINHE O NUMERO ---\n");
    printf("Eu escolhi um numero entre 1 e 100. Tente adivinhar!\n");

    while (palpite != numero_secreto) {
        printf("\nQual e o seu palpite? ");
        scanf("%d", &palpite);

        if (palpite < numero_secreto) {
            printf("Muito baixo! Tente um numero maior.\n");
        } else if (palpite > numero_secreto) {
            printf("Muito alto! Tente um numero menor.\n");
        }
    }

    printf("\nParabens! Voce acertou! O numero era %d.\n", numero_secreto);

    return 0;
}