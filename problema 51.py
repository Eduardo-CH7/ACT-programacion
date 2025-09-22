n = int(input("¿Cuántos trabajadores deseas registrar? "))

nombres = []
asistencias = []

for i in range(n):
    nombre = input(f"Nombre del trabajador {i+1}: ")
    asistencia = int(input(f"¿Asistió {nombre}? (1 = sí, 0 = no): "))
    nombres.append(nombre)
    asistencias.append(asistencia)

print("\nRegistro de asistencia:")
for i in range(n):
    if asistencias[i] == 1:
        print(f"{nombres[i]} asistió a trabajar")
    else:
        print(f"{nombres[i]} no asistió a trabajar")