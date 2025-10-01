def ordena_creciente(lista):
    return sorted(lista)

def ordena_decreciente(lista):
    return sorted(lista, reverse=True)

def elimina_por_indice(lista, indice):
    if 0 <= indice < len(lista):
        return lista.pop(indice)
    else:
        return "Índice fuera de rango"

def elimina_por_dato(lista, dato):
    if dato in lista:
        lista.remove(dato)
    return lista

def estadisticas(lista):
    if not lista:
        return None, None, None
    promedio = sum(lista) / len(lista)
    maximo = max(lista)
    minimo = min(lista)
    return promedio, maximo, minimo

# Programa principal
numeros = []
while True:
    print("\nMenú de opciones:")
    print("1. Agregar número")
    print("2. Ordenar creciente")
    print("3. Ordenar decreciente")
    print("4. Eliminar por índice")
    print("5. Eliminar por dato")
    print("6. Calcular promedio, máximo y mínimo")
    print("7. Mostrar lista actual")
    print("8. Salir")
    opcion = input("Elige una opción (1-8): ")

    if opcion == "1":
        num = float(input("Introduce el número a agregar: "))
        numeros.append(num)
    elif opcion == "2":
        numeros = ordena_creciente(numeros)
        print("Lista ordenada de forma creciente:", numeros)
    elif opcion == "3":
        numeros = ordena_decreciente(numeros)
        print("Lista ordenada de forma decreciente:", numeros)
    elif opcion == "4":
        idx = int(input("Introduce el índice a eliminar: "))
        eliminado = elimina_por_indice(numeros, idx)
        print("Valor eliminado:", eliminado)
    elif opcion == "5":
        dato = float(input("Introduce el dato a eliminar: "))
        numeros = elimina_por_dato(numeros, dato)
        print("Lista actualizada:", numeros)
    elif opcion == "6":
        promedio, maximo, minimo = estadisticas(numeros)
        print(f"Promedio: {promedio}, Máximo: {maximo}, Mínimo: {minimo}")
    elif opcion == "7":
        print("Lista actual:", numeros)
    elif opcion == "8":
        print("Programa finalizado.")
        break
    else:
        print("Opción no válida.")