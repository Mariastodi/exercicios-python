numeros = [1, 2, 3]
print("Lista inicial:")
for n in numeros:
    print(n)

numeros.append(4)
print("\nApós append(4):")
for n in numeros:
    print(n)

numeros[0] = 10
print("\nApós substituir o primeiro elemento:")
for n in numeros:
    print(n)

numeros.pop(2)
print("\nApós pop(2):")
for n in numeros:
    print(n)