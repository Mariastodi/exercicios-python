media = 1701.49
mediana = 1200.50

print(f"Média Aritmética: R$ {media:.2f}")
print(f"Mediana: R$ {mediana:.2f}")

if media > mediana:
    print("Análise: Média > Mediana. Indicação de assimetria positiva (outliers altos).")
elif media < mediana:
    print("Análise: Média < Mediana. Indicação de assimetria negativa (outliers baixos).")
else:
    print("Análise: Média = Mediana. Distribuição simétrica.")