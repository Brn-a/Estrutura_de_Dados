#include <iostream>
#include <cmath> // Para usar M_PI, que representa o valor de π

using namespace std;

int main() {
    double raio, altura, area;

    // Entrada de dados
    cout << "Digite o raio do cilindro: ";
    cin >> raio;

    cout << "Digite a altura do cilindro: ";
    cin >> altura;

    // Cálculo da área total
    area = 2 * M_PI * raio * (raio + altura);

    // Saída do resultado
    cout << "A área total do cilindro é: " << area << endl;

    return 0;
}