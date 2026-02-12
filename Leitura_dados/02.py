with open('dados_leitura.txt', 'w') as f:
    f.write('Esta é a primeira linha.\n')
    f.write('Esta é a segunda linha.')

arquivo = open('dados_leitura.txt', 'r')
conteudo = arquivo.read()
arquivo.close()

print("Conteúdo do arquivo:")
print(conteudo)