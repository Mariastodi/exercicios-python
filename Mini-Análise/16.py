import os

pasta = os.path.dirname(os.path.abspath(__file__))
csv_dados = os.path.join(pasta, 'dados_simples.csv')

print("Processando lista de registros...")

with open(csv_dados, 'r', encoding='utf-8') as f:
    next(f) 
    
    for linha in f:
        item = linha.strip().split(',')
        
        if len(item) == 3:
            nome = item[0]
            resultado = int(item[1]) + float(item[2])
            
            print(f"Nome: {nome:10} | Total: {resultado:.2f}")