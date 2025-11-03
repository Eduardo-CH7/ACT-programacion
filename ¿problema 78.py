
try:
    with open("datos.txt", "r", encoding="utf-8") as f:
        lineas = palabras = caracteres = 0
        for linea in f:
            lineas += 1
            palabras += len(linea.split())
            caracteres += len(linea)
    print(f"Líneas: {lineas}")
    print(f"Palabras: {palabras}")
    print(f"Caracteres: {caracteres}")
except FileNotFoundError:
    print("Error: el archivo 'datos.txt' no existe.")
except Exception as e:
    print("Error al leer el archivo:", e)