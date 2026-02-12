import os

diretorio = os.path.dirname(os.path.abspath(__file__))
csv_vendas = os.path.join(diretorio, 'vendas_ficticias.csv')

faturamentos = []

with open(csv_vendas, 'r', encoding='utf-8') as f:
    next(f)
    for linha in f:
        dados = linha.strip().split(',')
        if len(dados) >= 3:
            faturamentos.append(float(dados[1]) * int(dados[2]))

contagem = {}
for v in faturamentos:
    v_formatado = f"{v:.2f}"
    contagem[v_formatado] = contagem.get(v_formatado, 0) + 1

mais_frequente = None
max_repeticoes = 0

for valor, freq in contagem.items():
    if freq > max_repeticoes:
        max_repeticoes = freq
        mais_frequente = valor

if faturamentos:
    print(f"Moda: R$ {mais_frequente} | Repetições: {max_repeticoes}")
else:
    print("Nenhum dado processado.")