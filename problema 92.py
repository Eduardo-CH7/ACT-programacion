import re

texto = input("Introduce un párrafo: ").strip()
oraciones = re.split(r'(?<=[.!?])\s+', texto)

for oracion in oraciones:
    oracion = oracion.strip()
    if oracion:
        print(oracion)