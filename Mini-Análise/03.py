import os

pasta = os.path.dirname(os.path.abspath(__file__))
csv_vendas = os.path.join(pasta, 'vendas_ficticias.csv')

print("Resumo de Preços")

with open(csv_vendas, 'r', encoding='utf-8') as f:
    next(f) 
    
    for linha in f:
        dados = linha.strip().split(',')
        
        if len(dados) < 2:
            continue
            
        item = dados[0]
        preco = float(dados[1])
        
        print(f"Produto: {item:12} | Valor: R$ {preco:8.2f}")