#include <iostream>
#include <string> // para usar std::string

using namespace std;

int main() {
    string nome1, nome2;
    int idade1, idade2;

    // Entrada de dados
    cout << "Digite o nome da primeira pessoa: ";
    getline(cin, nome1); // permite nomes com espaços

    cout << "Digite a idade de " << nome1 << ": ";
    cin >> idade1;
    cin.ignore(); // limpa o buffer do teclado

    cout << "Digite o nome da segunda pessoa: ";
    getline(cin, nome2);

    cout << "Digite a idade de " << nome2 << ": ";
    cin >> idade2;

    // Comparação
    if (idade1 > idade2) {
        cout << nome1 << " é mais velho(a) que " << nome2 << "." << endl;
    } 
    else if (idade1 < idade2) {
        cout << nome2 << " é mais velho(a) que " << nome1 << "." << endl;
    } 
    else {
        cout << nome1 << " e " << nome2 << " têm a mesma idade." << endl;
    }

    return 0;
}
