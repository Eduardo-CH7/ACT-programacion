contraseña = input("Crea una contraseña: ")

intentos = 0
while intentos < 3:
    confirmacion = input("Vuelve a escribir la contraseña: ")
    if confirmacion == contraseña:
        print("¡Contraseña confirmada correctamente!")
        break
    else:
        intentos += 1
        if intentos == 3:
            print("Cuenta cancelada")
        else:
            print("Las contraseñas no coinciden. Intenta de nuevo.")