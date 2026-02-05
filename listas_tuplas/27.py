alunos = [
    {'nome': 'Carlos', 'nota': 8.5},
    {'nome': 'Beatriz', 'nota': 9.2},
    {'nome': 'Ana', 'nota': 7.8}
]


alunos_ordenados = sorted(alunos, key=lambda aluno: aluno['nota'], reverse=True)
print("Alunos ordenados pela maior nota:")
for aluno in alunos_ordenados:
     print(f"- {aluno['nome']}: {aluno['nota']}")
