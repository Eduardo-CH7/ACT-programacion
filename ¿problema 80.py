try:
    with open("origen.txt", "r", encoding="utf-8") as origen:
        with open("copia.txt", "w", encoding="utf-8") as destino:
            for linea in origen:
                destino.write(linea)
    print("Contenido copiado de 'origen.txt' a 'copia.txt'.")
except FileNotFoundError:
    print("Error: el archivo 'origen.txt' no existe.")
except Exception as e:
    print("Error al copiar el archivo:", e)
```
try:
    with open("origen.txt", "r", encoding="utf-8") as origen:
        with open("copia.txt", "w", encoding="utf-8") as destino:
            for linea in origen:
                destino.write(linea)
    print("Contenido copiado de 'origen.txt' a 'copia.txt'.")
except FileNotFoundError:
    print("Error: el archivo 'origen.txt' no existe.")
except Exception as e:
    print("Error al copiar el archivo:", e)