nombres = []
ahorros = []

n = int(input("¿Cuántos ahorradores deseas registrar? "))

for i in range(n):
    nombre = input(f"Nombre del ahorrador {i+1}: ")
    ahorro = float(input(f"Ahorro de {nombre}: "))
    nombres.append(nombre)
    ahorros.append(ahorro)

for i in range(n):
    if ahorros[i] < 1000:
        print(f"{nombres[i]} no tendrás para tu futuro")
    elif ahorros[i] > 1000000:
        print(f"{nombres[i]} ya merito te retiras")