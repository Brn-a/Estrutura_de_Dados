def maquina_de_sucos():
    """
    Função principal que executa a lógica da máquina de sucos.
    """
    print("--- BEM-VINDO À MÁQUINA DE SUCOS ---")
    print("Por favor, escolha sua bebida:")
    print("[1] Suco de Uva")
    print("[2] Suco de Maçã")
    print("[3] Suco de Laranja")
    print("--------------------------------------")

    try:
        opcao = int(input("Digite o número da opção desejada: "))
        
        print() 

        if opcao == 1:
            print("Você escolheu Suco de Uva. Ótima escolha, é refrescante!")
        elif opcao == 2:
            print("Você escolheu Suco de Maçã. Um clássico!")
        elif opcao == 3:
            print("Você escolheu Suco de Laranja. Rico em vitamina C!")
        else:
            print("Opção inválida! Por favor, escolha um número de 1 a 3.")

    except ValueError:
        print("\nEntrada inválida! Por favor, digite apenas o número da opção.")

    finally:
        print("\nObrigado por usar nossa máquina!")

maquina_de_sucos()