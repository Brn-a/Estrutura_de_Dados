nome1 = str(input("Digite o seu nome:\n"))
idade1 = int(input("Agora, digite sua idade:\n"))

nome2 = str(input("Digite o seu nome:\n"))
idade2 = int(input("Agora, digite sua idade:\n"))


if idade1 > idade2:
  print(nome1,"é mais velho(a)\n")
  print("E possui",idade1, "anos")
elif idade2 > idade1:
  print(nome2,"é mais velho(a)\n")
  print("E possui",idade2, "anos")
else:
  print("Ambos possuem a mesma idade")