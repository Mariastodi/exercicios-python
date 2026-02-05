def aplicar_operacao(a, b, operacao):
     return operacao(a, b)
 
def soma(x, y):
     return x + y
 
print(aplicar_operacao(5, 3, soma))