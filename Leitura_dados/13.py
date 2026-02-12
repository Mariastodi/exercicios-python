import csv
import json

cabecalho = ['produto', 'preco', 'estoque']
linhas_csv = [['Câmera', '350.90', '15'], ['Tripé', '85.20', '25']]

produtos_lista = []
for linha in linhas_csv:
    produto_dict = dict(zip(cabecalho, linha))
    produtos_lista.append(produto_dict)

with open('saida.json', 'w') as f:
    json.dump(produtos_lista, f, indent=4)

print("Dados convertidos e salvos em 'saida.json'.")