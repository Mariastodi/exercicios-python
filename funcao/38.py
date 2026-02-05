pessoas = [('Ana', 25), ('Bruno', 30), ('Carlos', 20)]
ordenado_por_idade = sorted(pessoas, key=lambda x: x[1])
print(f"Ordenado por idade: {ordenado_por_idade}")