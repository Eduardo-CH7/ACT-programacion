import re

texto = input("Introduce el texto: ")
patron = r'\b(0[1-9]|[12][0-9]|3[01])/(0[1-9]|1[0-2])/[0-9]{4}\b'
fechas = re.findall(patron, texto)


fechas_encontradas = [f"{d}/{m}/{y}" for d, m, y in fechas]

print("Fechas encontradas:", fechas_encontradas)