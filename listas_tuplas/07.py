lista = []  

itens = int(input("Quantos itens deseja adicionar? "))

for i in range(itens):
    nome = input(f"Qual o nome do item? ")
    lista.append(nome)

print("Lista de compras completa:")
for item in lista:
    print(f"- {item}")

remover = input("Deseja remover algum item? (sim/nao) ").lower() 
if remover == "sim":
    qual = input("Digite o nome do item que deseja excluir: ")
    if qual in lista:
        lista.remove(qual)
        print(f"O item '{qual}' foi removido com sucesso!")
    else:
        print("Item não encontrado na lista.")
else:
    print("Nenhum item foi removido.")

print("Lista final de compras:")
for item in lista:
    print(item)