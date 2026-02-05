numeros_pares = []
print("Antes do loop:", numeros_pares)

for numero in range(21):
    if numero % 2 == 0:
        numeros_pares.append(numero)

print("Depois do loop:", numeros_pares)