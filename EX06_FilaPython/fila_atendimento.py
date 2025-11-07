from collections import deque
fila = deque()

opcaoDesejada = 0

while opcaoDesejada != 4:

    opcaoDesejada = (int(input(
    "---MENU---\n"
    "1-Adicionar pessoa à fila\n2-Atender pessoa\n3-Mostrar fila\n4-Encerrar atendimento\n"
    "Escolha a opção desejada:"
    )))

    if opcaoDesejada == 1:
        nomePaciente = str(input("Digite o nome do paciente: "))
        fila.append(nomePaciente)
        print(f"Paciente {nomePaciente} adicionado à fila.")
        
    elif opcaoDesejada == 2:

        if fila:
            primeiroRemovido = fila.popleft()
            print(f"Paciente atendido: {primeiroRemovido}")
        else:

            print("A fila está vazia! Ninguém para atender.")
            
    elif opcaoDesejada == 3:

        if fila:
            print("Pessoas na fila:")

            for i, pessoa in enumerate(fila):
                print(f"{i+1}º: {pessoa}")
        else:

            print("A fila está vazia.")
            
    elif opcaoDesejada == 4:
        print("Encerrando o atendimento.")
    else:

        print("Opção inválida. Por favor, escolha uma das opções do menu.")