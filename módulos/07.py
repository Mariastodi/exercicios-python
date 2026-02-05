import math
import random
import datetime
import os

num = int(input("Digite um número inteiro para cálculos matemáticos: "))
fatorial = math.factorial(num)
raiz = math.sqrt(num)
print(f"O fatorial de {num} é: {fatorial}")
print(f"A raiz quadrada de {num} é: {raiz:.2f}")

nomes = ["Ana", "Bruno", "Carla", "Diego", "Elena"]
sorteado = random.choice(nomes)
print(f"\nLista de nomes: {nomes}")
print(f"O nome sorteado foi: {sorteado}")

agora = datetime.datetime.now()
ano_atual = agora.year
print(f"\nData e hora atuais: {agora.strftime('%d/%m/%Y %H:%M:%S')}")
print(f"Ano atual: {ano_atual}")

diretorio_atual = os.getcwd()
print(f"\nDiretório atual do script: {diretorio_atual}")

nome_pasta = "resultado_modulos"
if not os.path.exists(nome_pasta):
    os.makedirs(nome_pasta)
    print(f"Pasta '{nome_pasta}' criada com sucesso!")
else:
    print(f"A pasta '{nome_pasta}' já existe no diretório.")