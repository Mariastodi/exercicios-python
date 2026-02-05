alunos = ("Ana", "Pedro", "Maria")
for i, nome in enumerate(alunos): 
    print(f"Aluno na posição {i}: {nome}")

nomes_zip = ("Ana", "Pedro", "Maria")
notas = (9, 7, 8)
for nome, nota in zip(nomes_zip, notas): 
    print(f"{nome} tirou {nota}")
