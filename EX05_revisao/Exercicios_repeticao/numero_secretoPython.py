import random

def jogo_adivinhacao():
    """Função principal do jogo de adivinhar o número."""
    numero_secreto = random.randint(1, 100)
    palpite = 0

    print("--- JOGO: ADIVINHE O NÚMERO ---")
    print("Eu escolhi um número entre 1 e 100. Tente adivinhar!")

    while palpite != numero_secreto:
        try:
            palpite = int(input("\nQual é o seu palpite? "))

            if palpite < numero_secreto:
                print("Muito baixo! Tente um número maior.")
            elif palpite > numero_secreto:
                print("Muito alto! Tente um número menor.")

        except ValueError:
            print("Entrada inválida! Por favor, digite apenas um número.")

    print(f"\nParabéns! Você acertou! O número era {numero_secreto}.")


jogo_adivinhacao()