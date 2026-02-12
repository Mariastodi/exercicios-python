import json
usuario = {
    "nome": "Marcos Silva",
    "matricula": 20231045,
    "habilidades": ["Python", "Análise de Dados", "SQL"]
}

with open('cartao_usuario.json', 'w') as arquivo_saida:
    json.dump(usuario, arquivo_saida, indent=4)

with open('cartao_usuario.json', 'r') as arquivo_entrada:
    dados_carregados = json.load(arquivo_entrada)

print(f"Primeira habilidade: {dados_carregados['habilidades'][0]}")
print(f"Tipo de dado da variável carregada: {type(dados_carregados)}")