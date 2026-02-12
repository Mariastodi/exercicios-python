import os

pasta = os.path.dirname(os.path.abspath(__file__))
csv_vendas = os.path.join(pasta, 'vendas_ficticias.csv')

conteudo = [
    "Produto,Valor,Quantidade\n",
    "Celular,1200.50,2\n",
    "Notebook,3500.00,1\n",
    "Fone,150.99,5\n",
    "Mouse,50.00,3\n",
    "Teclado,120.00,1\n",
    "Webcam,85.50,4\n",
    "Monitor,950.00,1\n",
    "Cabo USB,15.00,10\n"
]

with open(csv_vendas, 'w', encoding='utf-8') as f:
    f.writelines(conteudo)

total_money = 0.0
total_items = 0

print(f"{'PRODUTO':<12} | {'UNITÁRIO':<10} | {'SUBTOTAL'}")
print("-" * 40)

with open(csv_vendas, 'r', encoding='utf-8') as f:
    next(f)
    for linha in f:
        row = linha.strip().split(',')
        if not row or len(row) < 3: continue
        
        nome, preco, qtd = row[0], float(row[1]), int(row[2])
        
        if preco <= 100.00:
            subtotal = preco * qtd
            total_money += subtotal
            total_items += qtd
            print(f"{nome:<12} | R$ {preco:>7.2f} | R$ {subtotal:>8.2f}")

print("-" * 40)
print(f"Itens de baixo custo vendidos: {total_items}")
print(f"Faturamento dessa categoria: R$ {total_money:.2f}")