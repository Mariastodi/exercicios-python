import os

pasta = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(pasta, 'vendas_ficticias.csv')

faturamentos = []

with open(caminho_csv, 'r', encoding='utf-8') as f:
    next(f)
    for linha in f:
        dados = linha.strip().split(',')
        if len(dados) >= 3:
            faturamentos.append(float(dados[1]) * int(dados[2]))

if faturamentos:
    faturamentos.sort()
    n = len(faturamentos)
    
    if n % 2 != 0:
        mediana = faturamentos[n // 2]
    else:
        mediana = (faturamentos[n // 2 - 1] + faturamentos[n // 2]) / 2
        
    print(f"Valores ordenados: {faturamentos}")
    print(f"Mediana: R$ {mediana:.2f}")
else:
    print("Nenhum dado para calcular a mediana.")