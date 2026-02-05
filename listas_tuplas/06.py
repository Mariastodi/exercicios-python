nome = input("Digite seu Nome: ")
idade = int(input("Digite sua Idade: "))
salario = float(input("Digite seu salário: "))

if idade >= 18 :
  print(f"Voce tem {idade} anos!!!! Está apto!!!! ")
else:
  print(f"Voce tem {idade} anos!!! Não está apto!!!")

salarioanual = salario * 12

print(f"Seu Salário Anual é de: {salarioanual}")
print("Relatório Final:")

print(f"Seu nome é: {nome}")
print(f"Sua idade é: {idade}")
print(f"Seu Salario é de : {salario}")
print(f"Voce ganha anualmente: {salarioanual}")