def processar_pedido(pedido, valor, acao_final):
     print(f"Preparando: {pedido}")
     print(f"Valor: R$ {valor}")
     acao_final(pedido, valor)

def entregar_balcao(pedido, valor):
    print(f"Pedido {pedido} pronto para retirada no balcão")

def entregar_delivery(pedido, valor):
     print(f"Pedido {pedido} saindo para entrega Taxa: R$ 5")
 
processar_pedido("Pizza Margherita", 25, entregar_balcao)
processar_pedido("Hambúrguer", 15, entregar_delivery)