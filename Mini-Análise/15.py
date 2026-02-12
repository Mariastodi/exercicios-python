conteudo = [
    "Nome,Idade,Altura_Metros\n",
    "Ana,25,1.65\n",
    "Bruno,30,1.80\n",
    "Carla,22,1.70\n"
]

with open('dados_simples.csv', 'w') as arquivo:
    arquivo.writelines(conteudo)