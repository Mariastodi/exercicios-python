def calcular_area_retangulo(largura, altura):
    area = largura * altura
    return area

def cadastrar_usuario(nome, idade, ativo=True):
    print(f"Usuário {nome}, {idade} anos - Ativo: {ativo}")

area_do_quarto = calcular_area_retangulo(5, 10)
print(area_do_quarto)

cadastrar_usuario("João", 27)