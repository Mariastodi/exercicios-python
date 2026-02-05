def somar(*numeros):
    return sum(numeros)

print(somar(1, 2, 3, 4))

def exibir_info(**dados):
    for chave, valor in dados.items():
        print(f"{chave}: {valor}")

exibir_info(nome="Ana", idade=25, cidade="Salvador")