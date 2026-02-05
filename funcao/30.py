def gerar_relatorio(tipo, inicio, fim=None, formato="PDF"):
     print(f"Relatório: {tipo}")
     print(f"Início: {inicio}, Fim: {fim}")
     print(f"Formato: {formato}")
 
gerar_relatorio("Vendas", "2025-08-01")
 
gerar_relatorio("Estoque", "2025-08-01", fim="2025-08-25", formato="Excel")