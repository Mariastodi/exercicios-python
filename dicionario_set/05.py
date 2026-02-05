vendas = {
    "Ana" : 10,
    "Bruno" : 15,
    "Carla" : 8,

}
vendas["Pedro"]= 12
del vendas["Carla"]
somavendas = sum(vendas.values())
print(f"{somavendas}")
print(vendas)