import json

dados_exemplo = {"user_id": 101, "atividade": "2023-10-27"}
with open('user_data.json', 'w') as f:
    json.dump(dados_exemplo, f)

with open('user_data.json', 'r') as arquivo_json:
    dados_usuario = json.load(arquivo_json)

print(f"ID do Usuário: {dados_usuario['user_id']}")
print(f"Última Atividade: {dados_usuario['atividade']}")