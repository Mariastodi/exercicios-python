import datetime
import time

def mostrar_horario():
    agora = datetime.datetime.now()
    print("Hora atual:", agora.strftime("%H:%M:%S"))

mostrar_horario()
time.sleep(2)
mostrar_horario()