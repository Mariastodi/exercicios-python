idade = int(input("Digite sua idade: "))
carteira = input("Voce possui carteira: (Exemplo sim ou não): ").lower().strip()

if idade >= 18 and carteira == "sim":
    print("Voce pode dirigir!!!")
else : 
    print("Nem a pau juvenal!!!!")