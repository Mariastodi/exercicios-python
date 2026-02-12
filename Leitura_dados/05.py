import csv

dados = [
    ['Produto', 'Preco', 'Estoque'],
    ['Monitor 24"', '850.50', '20'],
    ['Teclado Mecânico', '120.00', '5']
]

with open('produtos_basico.csv', 'w', newline='', encoding='utf-8') as arquivo:
    escritor_csv = csv.writer(arquivo)
    escritor_csv.writerows(dados)

print("Arquivo 'produtos_basico.csv' criado e pronto para leitura.")