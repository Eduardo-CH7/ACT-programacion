lista = [5, 8, 12, 20, 33, 45, 60, 77, 81, 99]
valor = int(input("Introduce el valor a buscar: "))

encontrado = False
for elemento in lista:
    if elemento == valor:
        encontrado = True
        break

if encontrado:
    print(f"El valor {valor} sí está en la lista.")
else:
    print(f"El valor {valor} no se encuentra en la lista.")