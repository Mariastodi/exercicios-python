import os

pasta = os.path.dirname(os.path.abspath(__file__))
caminho_csv = os.path.join(pasta, 'registros_vendas.csv')

if not os.path.exists(caminho_csv):
    with open(caminho_csv, 'w', encoding='utf-8') as f:
        f.write("Produto,Unidades_Vendidas,Preco_Unitario\n")
        f.write("Caneta,10,2.50\n")
        f.write("Caderno,2,25.00\n")
        f.write("Caneta,5,2.50\n")
        f.write("Lápis,20,1.00\n")
    print("-> Arquivo 'registros_vendas.csv' criado com sucesso!")

vendas_totais = 0
pedidos = 0
faturamento_caneta = 0.0

print("Processando registros de vendas...")

with open(caminho_csv, 'r', encoding='utf-8') as f:
    next(f) 
    
    for linha in f:
        row = linha.strip().split(',')
        
        if not row or len(row) < 3:
            continue
            
        item = row[0].strip()
        qtd = int(row[1])
        preco = float(row[2])
        
        vendas_totais += qtd
        pedidos += 1
        
        if item == "Caneta":
            faturamento_caneta += (qtd * preco)

print("-" * 30)
print(f"Volume total: {vendas_totais}")
print(f"Qtd Pedidos:  {pedidos}")
print(f"Total Canetas: R$ {faturamento_caneta:.2f}")