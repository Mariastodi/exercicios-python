import os

pasta_projeto = os.path.dirname(os.path.abspath(__file__))
caminho_vendas = os.path.join(pasta_projeto, 'vendas_ficticias.csv')

print("Calculando o faturamento por produto...")

with open(caminho_vendas, 'r', encoding='utf-8') as f:
    next(f)
    
    for linha in f:
        dados = linha.strip().split(',')
        
        if len(dados) < 3:
            continue
            
        item = dados[0]
        preco = float(dados[1])
        qtd = int(dados[2])
        
        total = preco * qtd
        
        print(f"Venda: {item} | Total: R$ {total:.2f}")