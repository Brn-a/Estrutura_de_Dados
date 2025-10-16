#include <stdio.h>
#define PI 3.14

int main() {
    float raio, altura, area;

    // Entrada de dados
    printf("Digite o raio do cilindro: ");
    scanf("%f", &raio);

    printf("Digite a altura do cilindro: ");
    scanf("%f", &altura);

    // Cálculo da área total
    area = 2 * PI * raio * (raio + altura);

    // Saída do resultado
    printf("A área total do cilindro é: %.2f\n", area);

    return 0;
}