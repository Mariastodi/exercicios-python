ARQUIVO = 'vendas_ficticias.csv'
print(f"Lendo o conteúdo do arquivo '{ARQUIVO}':")

with open(ARQUIVO, 'r') as arquivo:
    for linha in arquivo:
       
        print(linha.strip())