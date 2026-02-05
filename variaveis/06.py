nome=input("digite seu nome")
idade= int ( input ( "digite sua idade" ))
cidade=input('digite sua cidade')
peso=float(input("digite seu peso"))
altura=float(input("digite seu altura"))
   
imc= peso/ (altura*altura)

print (f"bem vindo {nome} de {cidade}. Sua idade e {idade} e seu imc e {imc:.2f} ")