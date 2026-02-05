import math
import random

filmes = [
    { "titulo": "Superman", "ano": 2025, "duracao_min": 129, "nota_imdb": 7.6 },
    { "titulo": "F1: The Movie", "ano": 2025, "duracao_min": 155, "nota_imdb": 7.9 },
    { "titulo": "Jurassic World: Rebirth", "ano": 2025, "duracao_min": 133, "nota_imdb": 6.0 },
    { "titulo": "Ice Road: Vengeance", "ano": 2025, "duracao_min": 112, "nota_imdb": 4.8 },
    { "titulo": "Highest 2 Lowest", "ano": 2025, "duracao_min": 133, "nota_imdb": 7.0 },
    { "titulo": "Quarteto Fantástico", "ano": 2025, "duracao_min": 126, "nota_imdb": 7.0 },
    { "titulo": "Guerreiras do K-Pop", "ano": 2025, "duracao_min": 95, "nota_imdb": 7.7 },
    { "titulo": "Uma Sexta-Feira Mais Louca", "ano": 2025, "duracao_min": 104, "nota_imdb": 6.9 }
]

total = len(filmes)
f_maior_nota = max(filmes, key=lambda f: f["nota_imdb"])
f_menor_nota = min(filmes, key=lambda f: f["nota_imdb"])
f_longo = max(filmes, key=lambda f: f["duracao_min"])
f_curto = min(filmes, key=lambda f: f["duracao_min"])

media_nota = math.fsum(f["nota_imdb"] for f in filmes) / total
media_duracao = math.fsum(f["duracao_min"] for f in filmes) / total

print("=== ANÁLISE DE DADOS DOS FILMES ===")
print(f"Total de filmes: {total}")
print(f"Maior nota: {f_maior_nota['nota_imdb']} - '{f_maior_nota['titulo']}'")
print(f"Menor nota: {f_menor_nota['nota_imdb']} - '{f_menor_nota['titulo']}'")
print(f"Mais longo: {f_longo['duracao_min']} min - '{f_longo['titulo']}'")
print(f"Mais curto: {f_curto['duracao_min']} min - '{f_curto['titulo']}'")

print("\n=== ANÁLISES MATEMÁTICAS ===")
print(f"Nota média: {media_nota:.2f}")
print(f"Duração média: {media_duracao:.1f} minutos")

print("\n=== RECOMENDAÇÕES ALEATÓRIAS ===")
recomendado = random.choice(filmes)
print(f"Filme aleatório: '{recomendado['titulo']}' ({recomendado['ano']})")

print("\nSugestão de maratona (3 filmes):")
maratona = random.sample(filmes, 3)
for i, f in enumerate(maratona, 1):
    print(f"{i}. {f['titulo']} - {f['duracao_min']} min")