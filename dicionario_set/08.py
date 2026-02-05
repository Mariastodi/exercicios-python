alunos = {}
while True :
    nome = input("Digite seu Nome ou Sair: " )
    if nome == "sair":
        break
    materias = {}
    while True:
        materia = input("Digite sua materia ou fim: ")
        if materia == "fim":
            break
        nota = float(input(f"Digite a nota da {materia}: "))
        materias[materia] = nota

    alunos[nome] = materias

print("\n ---Cadastro de Alunos---")
for aluno, notas in alunos.items():
    print(f"\nAluno: {aluno}")
    for materia , nota in notas.items():
        print(f"{materia}:{nota}")