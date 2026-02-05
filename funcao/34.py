def processar_notas(notas, quando_terminar):
     print("Processando notas...")
     media = sum(notas) / len(notas)
     quando_terminar(media) 

def mostrar_resultado(media):
     print(f"Resultado final: {media}")
 
def salvar_resultado(media):
     print(f"Média {media} salva no sistema")
 
notas = [8, 7, 9, 6, 8]
processar_notas(notas, mostrar_resultado)
processar_notas(notas, salvar_resultado)