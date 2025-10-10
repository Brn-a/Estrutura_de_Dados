print("--- Verificador de Números Primos ---")
numero = int(input("Digite um número inteiro maior que 1: "))

e_primo = True

if numero <= 1:
    e_primo = False
else:

    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            e_primo = False
            break 

if e_primo:
    print(f" O número {numero} é primo!")
else:
    print(f" O número {numero} não é primo.")