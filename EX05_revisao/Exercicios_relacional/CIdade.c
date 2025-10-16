#include <stdio.h>

int main() {
    char nome1[50], nome2[50];
    int idade1, idade2;

    // Entrada de dados
    printf("Digite o nome da primeira pessoa: ");
    scanf("%49s", nome1);

    printf("Digite a idade de %s: ", nome1);
    scanf("%d", &idade1);

    printf("Digite o nome da segunda pessoa: ");
    scanf("%49s", nome2);

    printf("Digite a idade de %s: ", nome2);
    scanf("%d", &idade2);

    // Comparação das idades
    if (idade1 > idade2) {
        printf("%s é mais velho(a) que %s.\n", nome1, nome2);
    } 
    else if (idade1 < idade2) {
        printf("%s é mais velho(a) que %s.\n", nome2, nome1);
    } 
    else {
        printf("%s e %s têm a mesma idade.\n", nome1, nome2);
    }

    return 0;
}