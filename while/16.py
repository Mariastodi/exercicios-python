cont = 1
guardar_o_valor = 0
while cont <= 5:
  nota = float(input("Digite uma nota: "))
  guardar_o_valor += nota
  cont += 1
media = guardar_o_valor / 5
print(media)