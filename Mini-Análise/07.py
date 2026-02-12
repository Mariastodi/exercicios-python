import os

pasta = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(pasta, 'vendas_ficticias.csv')

faturamentos = []

print("Extraindo dados de faturamento...")

with open(caminho_csv, 'r', encoding='utf-8') as f:
    next(f) 
    
    for linha in f:
        dados = linha.strip().split(',')
        
        if len(dados) >= 3:
            valor = float(dados[1]) * int(dados[2])
            faturamentos.append(valor)

if faturamentos:
    print(f"Valores coletados: {faturamentos}")
    print(f"Total de registros: {len(faturamentos)}")