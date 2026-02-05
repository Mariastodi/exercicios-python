def estatisticas(lista):
    minimo = min(lista)
    maximo = max(lista)
    media = sum(lista) / len(lista)
    return minimo, maximo, media

valores = [5, 10, 15]
print(estatisticas(valores))