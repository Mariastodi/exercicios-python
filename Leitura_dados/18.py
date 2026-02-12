import csv
import json

conteudo_csv = [
    ['ID', 'Nome', 'Preco_Unitario', 'Qtd_Estoque'],
    ['101', 'Caneta Azul', '2.50', '100'],
    ['102', 'Caderno A5', '15.00', ''], 
    ['103', 'Lápis HB', '1.00', '50'],
    ['104', 'Estojo', '20.00', '']       
]

with open('produtos_brutos.csv', 'w', newline='', encoding='utf-8') as f:
    escritor = csv.writer(f)
    escritor.writerows(conteudo_csv)

lista_produtos_limpos = []

with open('produtos_brutos.csv', 'r', newline='', encoding='utf-8') as f:
    leitor = csv.reader(f)
    cabecalho = next(leitor)  
    
    for linha in leitor:
      
        if linha[3] == '':
            continue  
        
        produto_dict = {
            "ID": int(linha[0]),
            "Nome": linha[1],
            "Preco_Unitario": float(linha[2]),
            "Qtd_Estoque": int(linha[3])
        }
        
     
        lista_produtos_limpos.append(produto_dict)

with open('produtos_limpos.json', 'w', encoding='utf-8') as f_json:
    json.dump(lista_produtos_limpos, f_json, indent=4, ensure_ascii=False)

print("Processamento concluído!")
print(f"Foram exportados {len(lista_produtos_limpos)} produtos para 'produtos_limpos.json'.")