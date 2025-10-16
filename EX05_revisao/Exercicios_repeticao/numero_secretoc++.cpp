#include <iostream>
#include <cstdlib> 
#include <ctime>   

int main() {
    srand(time(0)); 

    int numeroSecreto = (rand() % 100) + 1;
    int palpite = 0;

    std::cout << "--- JOGO: ADIVINHE O NUMERO ---" << std::endl;
    std::cout << "Eu escolhi um numero entre 1 e 100. Tente adivinhar!" << std::endl;

    while (palpite != numeroSecreto) {
        std::cout << "\nQual e o seu palpite? ";
        std::cin >> palpite;

        if (palpite < numeroSecreto) {
            std::cout << "Muito baixo! Tente um numero maior." << std::endl;
        } else if (palpite > numeroSecreto) {
            std::cout << "Muito alto! Tente um numero menor." << std::endl;
        }
    }

    std::cout << "\nParabens! Voce acertou! O numero era " << numeroSecreto << "." << std::endl;

    return 0;
}