def calcular_desconto(preco):
    taxa_desconto = 0.1
    return preco - (preco * taxa_desconto)

print(calcular_desconto(100))