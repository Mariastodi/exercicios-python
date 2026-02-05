import os                             

cwd = os.getcwd()                     
print("Diretório atual:", cwd)        

arquivos = os.listdir('.')            
print("Arquivos:", arquivos[:5])     

pasta = "dados_saida"
os.makedirs(pasta, exist_ok=True)     
print("Pasta criada (ou já existia):", pasta)