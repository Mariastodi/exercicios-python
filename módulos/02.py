import random                      

nomes = ["João", "Maria", "Pedro", "Ana"]
escolhido = random.choice(nomes)  
print("Escolhido:", escolhido)     

numero = random.randint(1, 10)     
print("Número:", numero)          

baralho = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
random.shuffle(baralho)            
print("Baralho embaralhado:", baralho[:5]) 