import re

texto = input("Introduce una cadena de texto: ")
patron = r'\d+\.\d+|\.\d+|\d+' 
coincidencias = re.findall(patron, texto)
numeros = [float(s) for s in coincidencias]

print(numeros)