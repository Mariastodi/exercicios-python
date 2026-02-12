import os

pasta = os.path.dirname(os.path.abspath(__file__))
planilha = os.path.join(pasta, 'vendas_ficticias.csv')

soma_vendas = 0.0
contagem = 0

print("Calculando totais do período...")

with open(planilha, 'r', encoding='utf-8') as f:
    next(f) 
    
    for linha in f:
        dados = linha.strip().split(',')
        
        if len(dados) < 3:
            continue
            
        preco = float(dados[1])
        qtd = int(dados[2])
        
        soma_vendas += (preco * qtd)
        contagem += 1

print(f"Vendas processadas: {contagem}")
print(f"Faturamento Total: R$ {soma_vendas:.2f}")