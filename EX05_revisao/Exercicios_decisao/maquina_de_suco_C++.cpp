#include <iostream>

int main() {
    int opcao;

    std::cout << "--- BEM-VINDO A MAQUINA DE SUCOS ---" << std::endl;
    std::cout << "[1] Suco de Uva, [2] Suco de Maca, [3] Suco de Laranja" << std::endl;
    std::cout << "Digite o numero da opcao desejada: ";
    std::cin >> opcao;
    std::cout << std::endl;

    if (opcao == 1) {
        std::cout << "Voce escolheu Suco de Uva. Otima escolha, e refrescante!" << std::endl;
    }
    else if (opcao == 2) {
        std::cout << "Voce escolheu Suco de Maca. Um classico!" << std::endl;
    }
    else if (opcao == 3) {
        std::cout << "Voce escolheu Suco de Laranja. Rico em vitamina C!" << std::endl;
    }
    else {
        std::cout << "Opcao invalida! Por favor, escolha um numero de 1 a 3." << std::endl;
    }

    std::cout << "\nObrigado por usar nossa maquina!" << std::endl;

    return 0;
}