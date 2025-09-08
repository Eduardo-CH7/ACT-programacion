while True:
    numero = int(input("Introduce un número entero entre 1 y 5: "))
    if 1 <= numero <= 5:
        print(f"¡Correcto! El número {numero} está en el rango.")
        break
    else:
        print("Número fuera de rango. Intenta de nuevo.")