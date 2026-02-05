total = 0

while True:
    preco = float(input("Digite o preço do item (0 para finalizar): R$ "))
    
    if preco == 0:
        break 
    
    total += preco  
    print(f"Subtotal acumulado: R$ {total:.2f}")

print(f"Total da compra: R$ {total:.2f}")