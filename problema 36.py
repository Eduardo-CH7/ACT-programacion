while True:
    numero = float(input("Introduce un número: "))
    cuadrado = numero ** 2
    print(f"El cuadrado de {numero} es {cuadrado}")
    repetir = input("¿Deseas ingresar otro número? (sí/no): ").strip().lower()
    if repetir != "sí":
        break