import csv

dados_iniciais = [['Nome', 'Valor'], ['A', '10.50']]
with open('novos_dados.csv', 'w', newline='') as f:
    csv.writer(f).writerows(dados_iniciais)

novo_registro = ['B', '22.75']
with open('novos_dados.csv', 'a', newline='') as arquivo_csv:
    escritor = csv.writer(arquivo_csv)
    escritor.writerow(novo_registro)

with open('novos_dados.csv', 'r', newline='') as f:
    for linha in csv.reader(f):
        print(f"Registro: {linha}")