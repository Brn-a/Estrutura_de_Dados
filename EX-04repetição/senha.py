senha_correta = "1234"
senha_digitada = input("Digite a senha: ")
while senha_digitada != senha_correta:
  print("Senha incorreta!")
  senha_digitada = input("Tente novamente: ")
print("Senha correta!")