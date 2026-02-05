alunos = []

alunos.append(("Ana", 20, 8.5))
alunos.append(("Bruno", 22, 7.0))
alunos.append(("Carla", 20, 9.2))

dicionario_alunos = {nome: (idade, nota) for nome, idade, nota in alunos}

def adicionar_aluno(nome, idade, nota):
    dicionario_alunos[nome] = (idade, nota)

def listar_alunos():
    for nome, (idade, nota) in dicionario_alunos.items():
        print(f"{nome} - Idade: {idade}, Nota: {nota}")

def media_notas():
    notas = [nota for idade, nota in dicionario_alunos.values()]
    return round(sum(notas) / len(notas),1)

def aluno_topo():
    return max(dicionario_alunos, key=lambda x: dicionario_alunos[x][1])

def idades_unicas():
    return {idade for idade, nota in dicionario_alunos.values()}

listar_alunos()
print("Média das notas:", media_notas())
print("Melhor aluno:", aluno_topo())
print("Idades únicas:", idades_unicas())
