print("¿Qué tipo de lista deseas crear?")
tipo = input("Escribe 'números' o 'texto': ").strip().lower()

if tipo == "números":
    lista = []
elif tipo == "texto":
    lista = []
else:
    print("Tipo de lista no válido.")
    exit()

while True:
    print("\nOpciones:")
    print("1. Agregar valores a la lista")
    print("2. Eliminar valores (por índice o por valor)")
    print("3. Ordenar la lista (modificándola directamente)")
    print("4. Ordenar la lista (nueva lista ordenada)")
    print("5. Verificar si un elemento está en la lista y mostrar índice(s)")
    if tipo == "números":
        print("6. Calcular máximo, mínimo, suma y promedio")
    print("7. Mostrar lista actual")
    print("8. Salir")
    opcion = input("Elige una opción (1-8): ")

    if opcion == "1":
        valor = input("Introduce el valor a agregar: ")
        if tipo == "números":
            try:
                valor = float(valor)
            except:
                print("Valor no válido.")
                continue
        lista.append(valor)
        print("Valor agregado.")
    elif opcion == "2":
        subop = input("¿Eliminar por índice (i) o por valor (v)?: ").strip().lower()
        if subop == "i":
            idx = int(input("Introduce el índice a eliminar: "))
            if 0 <= idx < len(lista):
                eliminado = lista.pop(idx)
                print(f"Elemento '{eliminado}' eliminado.")
            else:
                print("Índice fuera de rango.")
        elif subop == "v":
            valor = input("Introduce el valor a eliminar: ")
            if tipo == "números":
                try:
                    valor = float(valor)
                except:
                    print("Valor no válido.")
                    continue
            if valor in lista:
                lista.remove(valor)
                print(f"Elemento '{valor}' eliminado.")
            else:
                print("Valor no encontrado en la lista.")
        else:
            print("Opción no válida.")
    elif opcion == "3":
        lista.sort()
        print("Lista ordenada (modificada directamente).")
    elif opcion == "4":
        lista_ordenada = sorted(lista)
        print("Nueva lista ordenada:", lista_ordenada)
    elif opcion == "5":
        valor = input("Introduce el elemento a buscar: ")
        if tipo == "números":
            try:
                valor = float(valor)
            except:
                print("Valor no válido.")
                continue
        indices = [i for i, v in enumerate(lista) if v == valor]
        if indices:
            print(f"El elemento '{valor}' se encuentra en los índices: {indices}")
        else:
            print("Elemento no encontrado en la lista.")
    elif opcion == "6" and tipo == "números":
        if lista:
            print(f"Máximo: {max(lista)}")
            print(f"Mínimo: {min(lista)}")
            print(f"Suma: {sum(lista)}")
            print(f"Promedio: {sum(lista)/len(lista):.2f}")
        else:
            print("La lista está vacía.")
    elif opcion == "7":
        print("Lista actual:", lista)
    elif opcion == "8":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")