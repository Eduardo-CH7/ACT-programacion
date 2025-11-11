import re

email = input("Introduce un correo electrónico: ").strip()

patron = r'^[A-Za-z0-9]+@[A-Za-z0-9]+\.[A-Za-z]{2,}$'

if re.match(patron, email):
    print("Válido")
else:
    print("Inválido")