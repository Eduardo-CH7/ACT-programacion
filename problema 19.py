nombre = input("Introduce tu nombre: ")
boleta = input("Introduce tu número de boleta: ")

calificaciones = []
for i in range(1, 6):
    calificacion = float(input(f"Introduce la calificación {i}: "))
    calificaciones.append(calificacion)

promedio = sum(calificaciones) / len(calificaciones)

print(f"Nombre: {nombre}")
print(f"Boleta: {boleta}")
print(f"Promedio: {promedio:.2f}")