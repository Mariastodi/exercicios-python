def processar_lista(lista, funcao):
     return [funcao(item) for item in lista]
 
dados = [1, 2, 3, 4]

def dobra(elemento):
     return elemento * 2
 
def acrescenta(elemento):
     return elemento + 1

print("Elementos da lista dobrados:", processar_lista(dados, dobra))
print("Elementos da lista incrementados de 1:", processar_lista(dados, acrescenta))