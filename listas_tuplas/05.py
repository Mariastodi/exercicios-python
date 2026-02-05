frutas = [
    "Abacate", "Abacaxi", "Açaí", "Acerola", "Ameixa",
    "Amora", "Banana", "Cacau", "Cajá", "Caju",
    "Caqui", "Carambola", "Cereja", "Coco", "Cupuaçu",
    "Damasco", "Figo", "Framboesa", "Goiaba", "Graviola",
    "Groselha", "Guaraná", "Jabuticaba", "Jaca", "Jamelão",
    "Kiwi", "Laranja", "Lichia", "Limão", "Maçã",
    "Mamão", "Manga", "Maracujá", "Melancia", "Melão",
    "Mexerica", "Mirtilo", "Morango", "Nectarina", "Nêspera",
    "Pequi", "Pera", "Pêssego", "Pinha", "Pitanga",
    "Pitaya", "Romã", "Tamarindo", "Tangerina", "Uva",
    "Atemoia", "Bacaba", "Bacuri", "Baru", "Biribá",
    "Buriti", "Cabreúva", "Cabeludinha", "Cagaita", "Cambuci",
    "Camucamu", "Canistel", "Castanha-do-pará", "Ciriguela", "Cabeluda",
    "Duku", "Embaúba", "Feijoa", "Fruta-do-conde", "Fruta-pão",
    "Genipapo", "Grumixama", "Hurka", "Ingá", "Jambo",
    "Jenipapo", "Juatuba", "Jujuba", "Kinkan", "Lúcuma",
    "Maçã-do-amor", "Mamoncillo", "Mangaba", "Mangostão", "Mapati",
    "Marolo", "Marmelo", "Medronho", "Melão-de-são-caetano", "Moriche",
    "Murici", "Naranjilla", "Noni", "Oiti", "Olho-de-boi",
    "Pajurá", "Pau-brasil", "Pindo", "Pomelo", "Zimbro"
]

fruta_excluida = input("Digite o nome da fruta que você deseja remover: ")
fruta_encontrada = False

for fruta_da_vez in frutas:
  if fruta_da_vez == fruta_excluida:
    frutas.remove(fruta_da_vez)
    print(f"{fruta_excluida} removida com sucesso.")
    fruta_encontrada = True

if fruta_encontrada == False:
  print(f"{fruta_excluida} não encontrado")