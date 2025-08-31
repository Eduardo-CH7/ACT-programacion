total_preguntas = int(input("Introduce la cantidad total de preguntas del examen: "))
correctas = int(input("¿Cuántas preguntas contestaste correctamente?: "))

calificacion = (correctas / total_preguntas) * 10

print(f"Tu calificación final es: {calificacion:.2f}")