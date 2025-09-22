datos = []

for i in range(10):
    numero = float(input(f"Introduce el dato {i+1}: "))
    datos.append(numero)

print("Números elevados al cuadrado:")
for n in datos:
    print(n ** 2)