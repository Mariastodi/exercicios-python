paises_popul = {
    "Brasil": 215_000_000, 
    "China": 1_400_000_000,
    "EUA": 333_000_000, 
    "Índia": 1_220_000_000
}
 
pais_maior_popul = ""
maior_popul = 0

for nome, valor in paises_popul.items():
    if valor > maior_popul:
        maior_popul = valor
        pais_maior_popul = nome

print (f"O pais de maior população: {maior_popul} {pais_maior_popul}")