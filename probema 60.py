def sumatoria(lista):
    suma = 0
    for numero in lista:
        suma += numero
    return suma

def promedio(lista):
    if len(lista) == 0:
        return 0
    return sumatoria(lista) / len(lista)
