def calificacion_final(c1, c2, c3):
    promedio = (c1 + c2 + c3) / 3
    if promedio < 6:
        return f"{promedio:.2f} - te vas a extra"
    else:
        return f"{promedio:.2f}"
