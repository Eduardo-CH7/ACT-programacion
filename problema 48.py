n = int(input("¿Cuántos productos deseas ingresar? "))

nombres = []
claves = []
existencias = []

for i in range(n):
    nombre = input(f"Nombre del producto {i+1}: ")
    clave = input(f"Clave (código de barras) del producto {i+1}: ")
    existencia = int(input(f"Cantidad en existencia del producto {i+1}: "))
    nombres.append(nombre)
    claves.append(clave)
    existencias.append(existencia)

indice = int(input(f"\nIntroduce el índice del producto que deseas buscar (0 a {n-1}): "))

if 0 <= indice < n:
    print(f"\nInformación del producto en el índice {indice}:")
    print(f"Nombre: {nombres[indice]}")
    print(f"Clave: {claves[indice]}")
    print(f"Existencia: {existencias[indice]}")
else:
    print("Índice fuera de rango.")