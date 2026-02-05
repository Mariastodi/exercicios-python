from datetime import datetime
 
def formatar_data(data, formato='%d/%m/%Y'):
     return data.strftime(formato)
 
hoje = datetime(2025, 8, 26)

print(formatar_data(hoje))
 
print(formatar_data(hoje, formato='%Y-%m-%d'))