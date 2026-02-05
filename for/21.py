numero = int(input('Quantos produtos você irá cadastrar? '))
for i in range (numero):
   nome = input ('Qual o nome do produto? ')
   quantidade = int(input ('Qual a quantidade do produto? '))
   print (f"produto {nome} | quantidade {quantidade} ")