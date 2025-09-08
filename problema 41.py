contraseña = input("Crea una contraseña: ")

while True:
    confirmacion = input("Vuelve a escribir la contraseña: ")
    if confirmacion == contraseña:
        print("¡Contraseña confirmada correctamente!")
        break
    else:
        print("Las contraseñas no coinciden. Intenta de nuevo.")