palavra = input ('Digite uma palavra: ')
contador_vogais = 0 
vogais = 'aeiouAEIOU'
for i in palavra:
    if i in vogais:
        contador_vogais += 1
print (f'A soma das vogais da palavra escolhida é: {contador_vogais} ')