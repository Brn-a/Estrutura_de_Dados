palavra = input("Digite uma palavra: ")
vogais = "aeiouAEIOU"
contador_vogais = 0
for letra in palavra:
  if letra in vogais:
    contador_vogais += 1
print(f"\nA palavra '{palavra}' tem {contador_vogais} vogais.")