def executar_pipeline(dados, funcao):
    return [funcao(dado) for dado in dados]

def dobrar(numero):
    return numero * 2

def adicionar_5(numero):
    return numero + 5

dados = [1, 2, 3]

resultado1 = executar_pipeline(dados, dobrar)
print(f"Após dobrar: {resultado1}")

resultado2 = executar_pipeline(resultado1, adicionar_5)
print(f"Após adicionar 5: {resultado2}")