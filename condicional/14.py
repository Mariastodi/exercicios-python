n = int(input("Digite um Numero inteiro: "))
if n > 0:
    if n %2 ==0:
        print("Ele é Positivo e Par!!!!!")
    else :
        print("Ele é Positivo e Impar!!!!")
elif n < 0:
    if n %2 == 0:
        print("Ele é negativo e Par")
    else :
        print("Ele é Negativo e Impar")  
else :
    print("Ele é zero")