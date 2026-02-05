aluno1 = float(input("Digite sua nota "))
aluno2 = float(input("Digite sua nota "))
aluno3 = float(input("Digite sua nota "))
aluno4 = float(input("Digite sua nota "))

# soma = aluno1 + aluno2 + aluno3 + aluno4
# media = soma / 4

media = (aluno1 + aluno2 + aluno3 + aluno4) / 4
print(media)

if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")