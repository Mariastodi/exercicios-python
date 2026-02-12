with open('minhas_tarefas.txt', 'w') as arquivo:
    arquivo.write('Comprar material escolar\n')
    arquivo.write('Enviar relatório técnico\n')
    arquivo.write('Estudar sobre JSON\n')

with open('minhas_tarefas.txt', 'r') as arquivo:
    for linha in arquivo:
        
        print(f"[CONCLUIR] {linha.strip()}")