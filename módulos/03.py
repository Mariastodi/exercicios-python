from datetime import datetime, date, timedelta  

agora = datetime.now()              
print("Agora:", agora)             

hoje = date.today()                 
print("Dia:", hoje.day, "Mês:", hoje.month, "Ano:", hoje.year) 

formatada = agora.strftime("%d/%m/%Y %H:%M") 
print("Formatada:", formatada)

faz_7_dias = agora - timedelta(days=7)      
print("Há 7 dias:", faz_7_dias)