n = int(input("¿Cuántas materias deseas ingresar? "))

materias = []
calificaciones = []

for i in range(n):
    materia = input(f"Nombre de la materia {i+1}: ")
    calificacion = float(input(f"Calificación de {materia}: "))
    materias.append(materia)
    calificaciones.append(calificacion)

promedio = sum(calificaciones) / n

print("\nMaterias y calificaciones:")
for i in range(n):
    print(f"{materias[i]}: {calificaciones[i]}")

print(f"\nCalificación promedio: {promedio:.2f}")