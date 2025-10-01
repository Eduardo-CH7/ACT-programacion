def reprobados(nombres, calificaciones):
    lista_reprobados = []
    for i in range(len(nombres)):
        if calificaciones[i] < 6:
            lista_reprobados.append(nombres[i])
    return lista_reprobados