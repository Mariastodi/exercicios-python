senha = ""
tentativas = 0
while senha != "1234" and tentativas < 3:
    senha = input("Digite a senha: ")
    tentativas += 1

if senha == "1234":
    print("Acesso permitido")
else:
    print("Senha incorreta ou tentativas excedidas")