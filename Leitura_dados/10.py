import json

dados_config = {
    "tema": "dark",
    "versao": 2.1,
    "permissoes": ["leitura", "escrita"]
}

with open('config_app.json', 'w') as arquivo_json:
    json.dump(dados_config, arquivo_json, indent=4)

print("Arquivo 'config_app.json' criado com formatação JSON legível.")