frutas = ("banana", "pera", "limao", "maçã", "melancia")
print (f"Frutas Disponíveis {frutas}")

disponivel = input ("Qual fruta você deseja? ").lower()
if disponivel in frutas:
    print ("Fruta Disponível")
else:
    print ("Fruta não Disponível")
print (f"Total {len (frutas)}")