def contar_palavras(texto):
    palavras = texto.split()  
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

def palavras_unicas(dicionario):
    unicas = {palavra for palavra, qtd in dicionario.items() if qtd == 1}
    return unicas

texto = "maçã banana laranja maçã pera banana laranja laranja"

contagem = contar_palavras(texto)
unicas = palavras_unicas(contagem)

print("Contagem de palavras:")
print(contagem)
print("Palavras únicas:")
print(unicas)
