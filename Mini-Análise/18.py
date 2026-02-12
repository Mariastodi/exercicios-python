import os

pasta = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(pasta, 'registros_vendas.csv')

p_min = float('inf')
p_max = float('-inf')

print("Analisando preços unitários...")

with open(caminho_csv, 'r', encoding='utf-8') as f:
    next(f)
    
    for linha in f:
        row = linha.strip().split(',')
        
        if len(row) >= 3:
            preco = float(row[2])
            
            if preco < p_min:
                p_min = preco
            if preco > p_max:
                p_max = preco

if p_min != float('inf'):
    print("-" * 30)
    print(f"Preço Mínimo: R$ {p_min:.2f}")
    print(f"Preço Máximo: R$ {p_max:.2f}")
    print("-" * 30)
else:
    print("Arquivo sem dados para analisar.")