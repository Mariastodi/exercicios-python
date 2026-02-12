with open('lista_de_tarefas.txt', 'w') as f:
    f.write('Comprar pão\n')
    f.write('Pagar contas\n')
    f.write('Estudar Python')

with open('lista_de_tarefas.txt', 'r') as arquivo:
    linhas = arquivo.readlines()

print("As linhas do arquivo são:")
for linha in linhas:
    print(f"- {linha.strip()}") 