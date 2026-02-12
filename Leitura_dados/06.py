import csv

with open('dados_ponto_virgula.csv', 'w', newline='') as f:
    writer = csv.writer(f, delimiter=';')
    writer.writerow(['Nome', 'Idade'])
    writer.writerow(['Ana', '25'])
    writer.writerow(['Beto', '30'])

with open('dados_ponto_virgula.csv', 'r', newline='') as arquivo_csv:
    leitor = csv.reader(arquivo_csv, delimiter=';')
    print("Dados lidos:")
    for linha in leitor:
        print(f"Linha: {linha}")