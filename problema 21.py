evento = input("Introduce el nombre del evento: ")
fecha = input("Introduce la fecha del evento: ")
asistentes = int(input("Introduce el número de asistentes: "))

agua_total = asistentes * 1.5  # litros
carne_total = asistentes * 0.35  # kg (350 gramos = 0.35 kg)
salsa_total = agua_total * 0.25  # litros

print(f"Evento: {evento}")
print(f"Fecha: {fecha}")
print(f"Asistentes: {asistentes}")
print(f"Agua de jamaica necesaria: {agua_total:.2f} litros")
print(f"Carne necesaria: {carne_total:.2f} kg")
print(f"Salsa necesaria: {salsa_total:.2f} litros")