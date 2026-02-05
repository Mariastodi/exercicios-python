contador = 0
soma = 0
n = 5  
while contador < n:
    valor = float(input("Digite um número: "))
    soma += valor
    contador += 1

media = soma / n if n > 0 else 0
print("Média:", media)