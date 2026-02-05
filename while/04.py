n = int(input("Quantos números? "))
contador = 0
soma = 0
while contador < n:
    num = float(input("Digite um número: "))
    soma += num
    contador += 1

media = soma / n if n > 0 else 0
print("Média:", media)