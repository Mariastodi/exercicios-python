def desconto(preco):
    taxa = 0.1
    return preco - (preco * taxa)

preco = desconto(189)
print(preco)