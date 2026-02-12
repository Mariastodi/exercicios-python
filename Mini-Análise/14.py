import os

def gerar_relatorio(arquivo_csv):
    total = 0.0
    vendas = 0
    
    pasta = os.path.dirname(os.path.abspath(__file__))
    caminho = os.path.join(pasta, arquivo_csv)

    with open(caminho, 'r', encoding='utf-8') as f:
        next(f)  
        for linha in f:
            row = linha.strip().split(',')
            if len(row) >= 3:
                total += float(row[1]) * int(row[2])
                vendas += 1
                
    if vendas > 0:
        print(f"Relatório: {arquivo_csv}")
        print(f"Transações: {vendas}")
        print(f"Faturamento: R$ {total:.2f}")
        print(f"Média/Venda: R$ {total/vendas:.2f}")

gerar_relatorio('vendas_ficticias.csv')