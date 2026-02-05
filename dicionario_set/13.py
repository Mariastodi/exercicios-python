aluno = {
    "nome": "Bia",
    "curso": "Full Stack",
    "idade": 20

}

aluno ["idade"]+=1
aluno ["cidade"]="Natal"


email = aluno.get("email", "Não Informado")
aluno.pop ("curso")
print (aluno)

for chave, valor in aluno.items():
    print (f"{chave}:{valor}")