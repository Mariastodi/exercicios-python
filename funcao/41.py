def cadastrar_produtos():
    produtos = {
        "Camiseta": 50.00,
        "Tênis": 200.00,
        "Boné": 40.00,
        "Mochila": 120.00,
        "Jaqueta": 300.00
    }
    return produtos


def calcular_total(produtos, nome_produto, quantidade):
    if nome_produto not in produtos:
        return None
    return produtos[nome_produto] * quantidade


def aplicar_desconto(valor, tipo_pagamento):
    if tipo_pagamento.lower() == "pix":
        return valor * 0.90  
    elif tipo_pagamento.lower() == "debito":
        return valor * 0.95  
    elif tipo_pagamento.lower() == "credito":
        return valor 
    else:
        return None  


def processar_venda(nome_produto, quantidade, tipo_pagamento):
    produtos = cadastrar_produtos()

    total_sem_desconto = calcular_total(produtos, nome_produto, quantidade)
    if total_sem_desconto is None:
        return "Produto inválido!"

    valor_final = aplicar_desconto(total_sem_desconto, tipo_pagamento)
    if valor_final is None:
        return "Tipo de pagamento inválido!"

    return f"Produto: {nome_produto} | Quantidade: {quantidade} | Pagamento: {tipo_pagamento} | Valor final: R$ {valor_final:.2f}"

print(processar_venda("Camiseta", 2, "pix"))
print(processar_venda("Tênis", 1, "debito"))
print(processar_venda("Jaqueta", 1, "credito"))