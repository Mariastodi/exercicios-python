def calcular_preco(produto, quantidade):
      return produto['preco'] * quantidade
  
def aplicar_desconto(preco, quantidade):
      if quantidade > 10:
          return preco * 0.9
      return preco
  
def salvar_venda(cliente, valor):
    print(f"Salvando venda no banco: {cliente} R$ {valor}")
 
def enviar_confirmacao(cliente):
     print(f"Enviando email de confirmação para {cliente}")
 
def processar_venda(produto, quantidade, cliente):
     preco = calcular_preco(produto, quantidade)
     preco_final = aplicar_desconto(preco, quantidade)
     salvar_venda(cliente, preco_final)
     enviar_confirmacao(cliente)
     return preco_final
venda = processar_venda({'preco': 150}, 11, 'Linux')
print(venda)