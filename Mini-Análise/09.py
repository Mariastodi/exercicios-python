import os

pasta = os.path.dirname(os.path.abspath(__file__))
csv_vendas = os.path.join(pasta, 'vendas_ficticias.csv')

min_venda = float('inf')  
max_venda = float('-inf') 

print("Localizando extremos de faturamento...")

with open(csv_vendas, 'r', encoding='utf-8') as f:
    next(f)  
    
    for linha in f:
        dados = linha.strip().split(',')
        
        if len(dados) >= 3:
            valor = float(dados[1]) * int(dados[2])
            
            if valor < min_venda:
                min_venda = valor
            
            if valor > max_venda:
                max_venda = valor

if min_venda != float('inf'):
    print(f"Menor venda: R$ {min_venda:.2f}")
    print(f"Maior venda: R$ {max_venda:.2f}")
else:
    print("Nenhum dado processado.")