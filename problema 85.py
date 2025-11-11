import re

texto = input("Introduce una cadena de texto: ")
patron = r'\b[ÁÉÍÓÚA-ZÑ][a-záéíóúñÁÉÍÓÚÑ]*\b'
palabras = re.findall(patron, texto, flags=re.UNICODE)
print("Palabras que comienzan con mayúscula:", palabras)