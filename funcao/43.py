def numeros_pares(lista):    
    return [n for n in lista if n % 2 == 0]

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Usando função normal:", numeros_pares(numeros))

pares_lambda = list(filter(lambda x: x % 2 == 0, numeros))
print("Usando lambda + filter:", pares_lambda)
