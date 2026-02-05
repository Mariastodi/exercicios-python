produtos = [
    ("Maçã", 3.50, 4),
    ("Leite", 4.20, 2),
    ("Pão", 2.50, 6),
    ("Ovos", 0.80, 12)
]

for produto, preco_unitario, quantidade in produtos:
    preco_total = preco_unitario * quantidade
    print(f"{produto} - Quantidade: {quantidade}, Preço unitário: R${preco_unitario:.2f}, Preço total: R${preco_total:.2f}")
