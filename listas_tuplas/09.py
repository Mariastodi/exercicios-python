nomes = [] 
notas = [] 

for i in range(3):
    aluno = input("Digite o nome do aluno: ") 
    nota_aluno = float(input("Digite a nota: ")) 
    
    nomes.append(aluno)
    notas.append(nota_aluno)
    
print("Resultado ") 

for i in range(len(nomes)):
    if notas[i] >= 7:
        situacao = "Aprovado"
    elif notas[i] >= 5:
        situacao = "Recuperação"
    else:
        situacao = "Reprovado"
        
    print(f"Nome: {nomes[i]} | Nota: {notas[i]} | Situação: {situacao}")