from functools import reduce
 
dados = [1, 2, 3, 4, 5]
 
dobrar = list(map(lambda x: x * 2, dados)) 

pares = list(filter(lambda x: x % 2 == 0, dados))
 
soma_total = reduce(lambda acumulador, atual: acumulador + atual, dados)
 
print(f"Dados originais: {dados}")
print(f"MAP (Dobro): {dobrar}")
print(f"FILTER (Pares): {pares}")
print(f"REDUCE (Soma): {soma_total}")
