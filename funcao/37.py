def buscar_saldo(conta):
    return 1000 

def realizar_saque(conta, valor):
    saldo = buscar_saldo(conta)
    if valor <= saldo:
        print(f"Saque de R$ {valor} aprovado")
        return True
    else:
        print("Saldo insuficiente")
        return False

def solicitar_saque(valor):
    conta = "12345"
    valor = valor
    realizar_saque(conta, valor)

solicitar_saque(500)