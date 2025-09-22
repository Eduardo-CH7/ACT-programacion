datos = []

while True:
    dato = input("Introduce un dato: ")
    datos.append(dato)
    continuar = input("¿Deseas ingresar otro dato? (sí/no): ").strip().lower()
    if continuar != "sí":
        break

datos_ordenados = sorted(datos)
print("Lista ordenada:", datos_ordenados)