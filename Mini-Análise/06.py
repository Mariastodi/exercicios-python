import os

pasta = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(pasta, 'vendas_ficticias.csv')

vendas_totais = 0
pedidos = 0

print("Analizando volume de vendas...")

with open(caminho_csv, 'r', encoding='utf-8') as f:
    next(f) 
    
    for linha in f:
        row = linha.strip().split(',')
        
        if len(row) >= 3:
            
            vendas_totais += int(row[2])
            pedidos += 1

print(f"Pedidos processados: {pedidos}")
print(f"Volume total de itens: {vendas_totais}")