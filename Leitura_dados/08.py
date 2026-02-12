import csv

dados_vendas = [
    ['Produto', 'Preco', 'Estoque'],
    ['Câmera', '350.90', '15'],
    ['Tripé', '85.20', '25']
]

with open('dataset_vendas.csv', 'w', newline='') as f:
    csv.writer(f).writerows(dados_vendas)

with open('dataset_vendas.csv', 'r', newline='') as arquivo_csv:
    leitor = csv.reader(arquivo_csv)
    cabecalho = next(leitor) 
    print(f"Cabeçalho lido (e pulado): {cabecalho}")
    
    for linha in leitor:
        produto, preco_str, estoque_str = linha
        valor_total = float(preco_str) * int(estoque_str)
        print(f"Produto: {produto} | Valor Total em Estoque: R${valor_total:.2f}")