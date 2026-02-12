import json

dados_python = {
    "empresa": "Tech Solutions",
    "funcionarios": [
        {"nome": "Carlos", "cargo": "Analista"},
        {"nome": "Sofia", "cargo": "Desenvolvedora"}
    ],
    "ativo": True
}

json_string = json.dumps(dados_python, indent=4)
print("Estrutura JSON gerada:")
print(json_string)