def aplicar_desconto(preco, tipo_desconto):
      return tipo_desconto(preco)
  
def desconto_estudante(preco):
      return preco * 0.9  
  
def desconto_cliente_vip(preco):
      return preco * 0.8  
  
def desconto_black_friday(preco):
     return preco * 0.7  
 
preco_original = 100

tipo_desconto = {
     'estudante': desconto_estudante,
     'vip': desconto_cliente_vip,
     'black_friday': desconto_black_friday
}

usuario_desconto = input("Digite o tipo do seu desconto (estudante, vip, black_friday): ")
preco_com_desconto = aplicar_desconto(preco_original, tipo_desconto[usuario_desconto]) 
print(f"{usuario_desconto.capitalize()} paga: R$ {preco_com_desconto}")