senha = ""
tentativas = 0
limite_tentativas = 3

while senha != "1234" and tentativas < limite_tentativas:
    senha = input("tenta ai: ")
    if senha != "1234":
        tentativas += 1
        if tentativas < limite_tentativas:
            print(f"Senha incorreta. Você tem mais {limite_tentativas - tentativas} tentativas.")
        else:
            print("Senha incorreta. Limite de tentativas atingido.")

if senha == "1234":
    print("finalmente ne vei")
else:
    print("Acesso bloqueado.")