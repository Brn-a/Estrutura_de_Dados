from collections import deque

historico = deque()
opcao = 0

while opcao != 5:

    print("\n--- NAVEGADOR WEB ---")
    
    if historico:
        print(f"[Você está na página: {historico[-1]}]")
    else:
        print("[Você está na página inicial (vazia)]")

    opcao = (int(input(
        "1- Visitar nova página\n"
        "2- Voltar (página anterior)\n"
        "3- Ver histórico completo\n"
        "4- Limpar histórico\n"
        "5- Fechar navegador\n"
        "Escolha a opção desejada: "
    )))

    if opcao == 1:
        nova_pagina = input("Digite o URL da nova página: ")
        historico.append(nova_pagina)
        print(f"Navegando para {nova_pagina}...")
        
    elif opcao == 2:
        if historico:
            pagina_removida = historico.pop()
            print(f"Saindo da página '{pagina_removida}'...")
            if historico:
                print(f"Você voltou para '{historico[-1]}'.")
            else:
                print("Você voltou para a página inicial.")
        else:
            print("Não há para onde voltar. O histórico está vazio.")
            
    elif opcao == 3:
        if historico:
            print("\n--- Histórico de Navegação ---")
            for i, pagina in enumerate(historico):
                print(f"{i+1}º: {pagina}")
        else:
            print("O histórico está vazio.")
    
    elif opcao == 4:
        historico.clear()
        print("Histórico limpo.")
            
    elif opcao == 5:
        print("Fechando o navegador.")
        
    else:
        print("Opção inválida. Por favor, escolha uma das opções do menu.")