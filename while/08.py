soma = 0
while True:
    num = float(input("Digite um número (0 para encerrar): "))
    if num == 0:
        break
    soma += num
print("Soma total:", soma)