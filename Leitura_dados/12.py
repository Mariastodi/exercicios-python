
dados_sujos = [['Produto A', '100.0', '2'], ['Produto B', '', '5'], ['Produto C', '250.0', '']]
dados_limpos = []

for linha in dados_sujos:
    nome = linha[0]
    preco = float(linha[1]) if linha[1] else 0.0
    qtd = int(linha[2]) if linha[2] else 0
    dados_limpos.append([nome, preco, qtd])

print(f"Dados Limpos: {dados_limpos}")