import re

texto = input("Introduce el texto con correos: ")
patron = r'([A-Za-z0-9._%+-]+)@(?:[A-Za-z0-9.-]+\.[A-Za-z]{2,})'
usuarios = re.findall(patron, texto)

if usuarios:
    print("Nombres de usuario encontrados:", usuarios)
else:
    print("No se encontraron nombres de usuario.")