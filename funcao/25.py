def soma(numero1, numero2):
    return numero1 + numero2

def subtracao(numero1, numero2):
    return numero1 - numero2

def multiplicacao(numero1, numero2):
    return numero1 * numero2

def divisao(numero1, numero2):
    return numero1 / numero2

operacao = input("\nDigite o tipo de operação que deseja fazer:\nsoma,\nsubtração, \nmultiplicação, \ndivisão\n\n").lower()

n1 = int(input("Digite o primeiro número:"))

n2 = int(input("Digite o segundo número:"))

if operacao == 'soma':
    resultado = soma(n1, n2)
elif operacao == 'subtração':
    resultado = subtracao(n1, n2)
elif operacao == 'divisão':
    resultado = divisao(n1, n2)
else:
    resultado = multiplicacao(n1, n2)


print(f"O resultado da {operacao} foi {resultado}")