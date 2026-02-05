def cadastro(**kwargs):
    for chave, valor in kwargs.items():
        print(f"{chave}: {valor}")

cadastro(nome="João", idade=30, cidade="Recife")