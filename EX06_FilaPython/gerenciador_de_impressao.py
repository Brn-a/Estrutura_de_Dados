import time
from collections import deque

fila_impressao = deque()
opcao = 0

while opcao != 4:
    print("\n--- 🖨️ GERENCIADOR DE IMPRESSÃO ---")
    print("1. Adicionar documento à fila")
    print("2. Imprimir próximo documento")
    print("3. Ver fila de impressão")
    print("4. Sair")

    try:
        opcao = int(input("Escolha sua opção: "))
    except ValueError:
        print("Erro: Por favor, digite um número.")
        continue 

    if opcao == 1:
        nome_doc = input("Digite o nome do documento (ex: 'Relatorio.pdf'): ")
        fila_impressao.append(nome_doc)
        print(f"Documento '{nome_doc}' foi adicionado à fila.")

    elif opcao == 2:
        if fila_impressao: 
            documento_atual = fila_impressao.popleft()
            print(f"\nImprimindo '{documento_atual}'...")
            time.sleep(2) 
            print(f"'{documento_atual}' foi impresso com sucesso!")
        else:
            print("\nA fila de impressão está vazia. Nenhum documento para imprimir.")

    elif opcao == 3:
        if fila_impressao:
            print("\nDocumentos aguardando impressão:")
            for i, doc in enumerate(fila_impressao):
                print(f"  {i+1}º na fila: {doc}")
        else:
            print("\nA fila de impressão está vazia.")

    elif opcao == 4:
        print("Encerrando o gerenciador de impressão.")

    else:
        print("Opção inválida. Tente novamente.")