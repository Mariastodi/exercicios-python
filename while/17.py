cont = 1
guardar_o_valor = 0
qtde_notas = int(input("Digite quantas notas você quer calcular: "))
while cont <= qtde_notas:
  nota = float(input("Digite uma nota: "))
  guardar_o_valor += nota
  cont += 1
media = guardar_o_valor / qtde_notas
print(media)