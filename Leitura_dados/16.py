import csv

dados = [
    ['S01', '10.5', '12.3'],
    ['S02', '20.0', '18.5'],
    ['S03', '15.2', '14.8']
]

with open('dados_desempenho.csv', 'w', newline='') as arquivo_escrita:
    escritor = csv.writer(arquivo_escrita)
    escritor.writerow(['ID', 'Leitura_1', 'Leitura_2']) 
    escritor.writerows(dados)

with open('dados_desempenho.csv', 'r', newline='') as arquivo_leitura:
    leitor = csv.reader(arquivo_leitura)
    
  
    next(leitor)
    
    print("--- Desempenho dos Sensores ---")
    for linha in leitor:
   
        sensor_id = linha[0]
        l1 = float(linha[1]) 
        l2 = float(linha[2]) 
        
 
        media = (l1 + l2) / 2
        
        print(f"Sensor: {sensor_id} | Média: {media:.2f}")