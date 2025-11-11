import re

contrasena = input("Introduce la contraseña: ")

if (
    len(contrasena) >= 8
    and re.search(r"[A-Z]", contrasena)
    and re.search(r"[a-z]", contrasena)
    and re.search(r"\d", contrasena)
):
    print("Contraseña segura")
else:
    print("Insegura")