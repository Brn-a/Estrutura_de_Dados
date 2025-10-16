import math

altura = float(input("Digite a altura do cilindro: "))  
raio = float(input("Digite o raio do cilindro: "))       

resultado = 2 * math.pi * raio * (raio + altura)

print("A área total do cilindro é: {:.2f}".format(resultado))