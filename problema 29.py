dividendo = float(input("Introduce el dividendo: "))
divisor = float(input("Introduce el divisor: "))

if divisor == 0:
    print("Error: No se puede dividir entre cero.")
else:
    resultado = dividendo / divisor
    print(f"El resultado de la división es: {resultado}")