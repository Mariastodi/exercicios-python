quadrados = tuple(x**2 for x in range(5)) 
print(f"Tupla de quadrados: {quadrados}") 

palavra = "Python"
letras_maiusculas = tuple(letra.upper() for letra in palavra)
print(f"Tupla de letras maiúsculas: {letras_maiusculas}")
