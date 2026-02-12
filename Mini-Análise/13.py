import os

diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(diretorio, 'vendas_ficticias.csv')

limite_preco = 1000.0
alvo = 'Notebook'
soma_filtrada = 0.0

print(f"Filtrando vendas de {alvo} acima de R$ {limite_preco}...")

with open(caminho_csv, 'r', encoding='utf-8') as f:
    next(f) 
    
    for linha in f:
        dados = linha.strip().split(',')
        
        if len(dados) < 3:
            continue
            
        item = dados[0]
        preco = float(dados[1])
        qtd = int(dados[2])
        
        if item == alvo and preco > limite_preco:
            soma_filtrada += (preco * qtd)
            print(f"Venda encontrada: {item} - Total: R$ {preco * qtd:.2f}")

print(f"Faturamento total de {alvo}: R$ {soma_filtrada:.2f}")