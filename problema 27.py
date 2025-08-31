opcion = input("¿Qué deseas calcular? Escribe 'área' o 'perímetro': ").strip().lower()
lado = float(input("Introduce el valor del lado del cuadrado (número positivo): "))

if lado <= 0:
    print("El valor del lado debe ser un número positivo.")
elif opcion == "área":
    area = lado * lado
    print(f"El área del cuadrado es: {area}")
elif opcion == "perímetro":
    perimetro = 4 * lado
    print(f"El perímetro del cuadrado es: {perimetro}")
else:
    print("Opción no válida. Debes escribir 'área' o 'perímetro'.")