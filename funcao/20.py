def saque(saldo_atual, valor_saque):
    if valor_saque <= saldo_atual:
        novo_saldo = saldo_atual - valor_saque
        print(f"Saque de R$ {valor_saque:.2f} realizado com sucesso!")
        print(f"Novo saldo: R$ {novo_saldo:.2f}")
    else:
        print("Saldo insuficiente.")
        print(f"Saldo atual: R$ {saldo_atual:.2f}")

saque(500, 200)
saque(100, 150)