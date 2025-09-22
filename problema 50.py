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
    print("2. Buscar producto por nombre")
    print("3. Buscar producto por clave")
    print("4. Mostrar todos los productos")
    print("5. Salir")
    opcion = input("Elige una opción (1-5): ")

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
        nombre_buscar = input("Introduce el nombre del producto a buscar: ")
        if nombre_buscar in nombres:
            idx = nombres.index(nombre_buscar)
            print(f"\nInformación del producto '{nombre_buscar}':")
            print(f"Índice: {idx}")
            print(f"Clave: {claves[idx]}")
            print(f"Existencia: {existencias[idx]}")
        else:
            print("Producto no encontrado.")
    elif opcion == "3":
        clave_buscar = input("Introduce la clave del producto a buscar: ")
        if clave_buscar in claves:
            idx = claves.index(clave_buscar)
            print(f"\nInformación del producto con clave '{clave_buscar}':")
            print(f"Índice: {idx}")
            print(f"Nombre: {nombres[idx]}")
            print(f"Existencia: {existencias[idx]}")
        else:
            print("Clave no encontrada.")
    elif opcion == "4":
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
    elif opcion == "5":
        break
    else:
        print("Opción no válida.")