from collections import deque
pilha = deque()

opcaoDesejada = 0

while opcaoDesejada != 5:

    opcaoDesejada = (int(input(
        "---MENU---\n"
        "1-Adicionar ingrediente na pilha\n"
        "2-remover ingrediente do topo\n"
        "3-Mostrar ultimo ingrediente adicionado\n"
        "4-Mostra sanduiche\n"
        "5-Finalizar pedido\n"
        "Escolha a opção desejada: "
    )))

    if opcaoDesejada == 1:
        ingrediente = str(input("Digite o nome do ingrediente: "))
        pilha.append(ingrediente)
        print(f"Ingrediente {ingrediente} adicionado à pilha.")
        
    elif opcaoDesejada == 2:
        if pilha:
            ultimoRemovido = pilha.pop()
            print(f"Ingrediente removido: {ultimoRemovido}")
        else:
            print("O pedido está vazio, nenhum ingrediente foi adicionado.")
            
    elif opcaoDesejada == 3:
        if pilha:
            print(f"Ultimo ingrediente adicionado: {pilha[-1]}")
        else:
            print("A pilha está vazia.")
    
    elif opcaoDesejada == 4:
        if pilha:
            print("Ingredientes do sanduíche:")

            for i, ingrediente in enumerate(pilha):
                print(f"{i+1}º: {ingrediente}")
        else:
            print("O pedido está vazio, nenhum ingrediente foi adicionado.")    
            
    elif opcaoDesejada == 5:
        print("Pedido finalizado.")
        
    else:
        print("Opção inválida. Por favor, escolha uma das opções do menu.")