nome_arquivo = 'log_diario.txt'

with open(nome_arquivo, 'w') as f:
    f.write('08:00 Sistema iniciado.\n')

with open(nome_arquivo, 'a') as f:
    f.write('10:30 Processamento de dados iniciado.\n')

with open(nome_arquivo, 'r') as f:
    print("Conteúdo do log final:")
    print(f.read())