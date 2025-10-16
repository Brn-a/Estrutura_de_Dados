#include <stdio.h>

int main() {
    int opcao;

    printf("--- BEM-VINDO A MAQUINA DE SUCOS ---\n");
    printf("[1] Suco de Uva, [2] Suco de Maca, [3] Suco de Laranja\n");
    printf("Digite o numero da opcao desejada: ");
    scanf("%d", &opcao);
    printf("\n");

    if (opcao == 1) {
        printf("Voce escolheu Suco de Uva. Otima escolha, e refrescante!\n");
    } 
    else if (opcao == 2) {
        printf("Voce escolheu Suco de Maca. Um classico!\n");
    } 
    else if (opcao == 3) {
        printf("Voce escolheu Suco de Laranja. Rico em vitamina C!\n");
    } 
    else {
        printf("Opcao invalida! Por favor, escolha um numero de 1 a 3.\n");
    }

    printf("\nObrigado por usar nossa maquina!\n");

    return 0;
}