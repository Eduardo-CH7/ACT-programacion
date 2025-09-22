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

while True:
    print("\nOpciones:")
    print("1. Buscar producto por índice")
    print("2. Mostrar todos los productos")
    print("3. Salir")
    opcion = input("Elige una opción (1-3): ")

    if opcion == "1":
        indice = int(input(f"Introduce el índice del producto que deseas buscar (0 a {n-1}): "))
        if 0 <= indice < n:
            print(f"\nInformación del producto en el índice {indice}:")
            print(f"Nombre: {nombres[indice]}")
            print(f"Clave: {claves[indice]}")
            print(f"Existencia: {existencias[indice]}")
        else:
            print("Índice fuera de rango.")
    elif opcion == "2":
        productos = {}
        for i in range(n):
            productos[i] = {
                "nombre": nombres[i],
                "clave": claves[i],
                "existencia": existencias[i]
            }
        print("\nTodos los productos almacenados:")
        for idx, info in productos.items():
            print(f"Índice {idx}: {info}")
    elif opcion == "3":
        break
    else:
        print("Opción no válida.")