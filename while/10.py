while True:
    print("1 - Olá")
    print("2 - Soma")
    print("3 - Sair")
    escolha = input("Escolha: ")
    if escolha == "1":
        print("Olá!")
    elif escolha == "2":
        a = int(input("a: "))
        b = int(input("b: "))
        print("Soma:", a + b)
    elif escolha == "3":
        break
    else:
        print("Opção inválida")