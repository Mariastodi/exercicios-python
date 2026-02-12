import os

diretorio = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(diretorio, 'vendas_ficticias.csv')

faturamentos = []

with open(caminho_csv, 'r', encoding='utf-8') as f:
    next(f)  
    for linha in f:
        dados = linha.strip().split(',')
        if len(dados) >= 3:
            valor_venda = float(dados[1]) * int(dados[2])
            faturamentos.append(valor_venda)

soma_total = 0
for valor in faturamentos:
    soma_total += valor

if faturamentos:
    quantidade_valores = len(faturamentos)
    media = soma_total / quantidade_valores
    print(f"Soma Total dos Faturamentos: R$ {soma_total:.2f}")
    print(f"Média de Faturamento por Transação: R$ {media:.2f}")
else:
    print("Nenhum dado para calcular a média.")