
from datetime import datetime
def calcular_dias(f1,f2):
	#definir el formato de la fecha
	formato = "%d/%m/%Y"
	f1 = datetime.strptime(f1, formato)
	f2 = datetime.strptime(f2, formato)
	diferencia = f2 - f1
	return diferencia.days

f1 = input("fecha 1: ")
f2 = input("fecha 2: ")
dias = calcular_dias(f1,f2)
print("Hay",dias, "dias de diferencia entre las dos fechas ingresadas")

