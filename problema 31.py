calificacion = float(input("Introduce la calificación (0 a 10): "))

if calificacion < 0 or calificacion > 10:
    print("Error: La calificación debe estar entre 0 y 10.")
elif calificacion < 6:
    print("Situación académica: Irregular")
elif 6 <= calificacion < 10:
    print("Situación académica: Regular")
elif calificacion == 10:
    print("Situación académica: Excelencia")