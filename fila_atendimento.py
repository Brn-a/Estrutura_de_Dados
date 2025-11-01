
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
        print(f"fila{fila}")
    elif opcaoDesejada == 2:
        primeiroRemovido = fila.popleft()
        print(f"paciente atendido: {primeiroRemovido}")  
    elif opcaoDesejada == 3:
        print(fila)
        
