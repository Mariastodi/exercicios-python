ARQUIVO = 'vendas_ficticias.csv'

dados_csv = [
    "Produto, Valor, Quantidade\n",
    "Celular, 1200.50,2\n",
    "Notebook, 3500.00,1\n",
    "Fone, 150.99,5\n",
    "Mouse, 50.00,3\n"
]

with open(ARQUIVO, 'w') as arquivo:
    arquivo.writelines(dados_csv)

print(f"Arquivo {ARQUIVO} criado com sucesso para a prática.")