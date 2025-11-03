try:
    with open("a.txt", "r", encoding="utf-8") as fa, open("b.txt", "r", encoding="utf-8") as fb:
        contenido = fa.read() + fb.read()

    with open("combinado.txt", "w", encoding="utf-8") as fc:
        fc.write(contenido)

    print("Archivos combinados en 'combinado.txt'.")
except FileNotFoundError as e:
    print(f"Error: archivo no encontrado: {e.filename}")
except Exception as e:
    print("Error al combinar archivos:", e)
```try:
    with open("a.txt", "r", encoding="utf-8") as fa, open("b.txt", "r", encoding="utf-8") as fb:
        contenido = fa.read() + fb.read()

    with open("combinado.txt", "w", encoding="utf-8") as fc:
        fc.write(contenido)

    print("Archivos combinados en 'combinado.txt'.")
except FileNotFoundError as e:
    print(f"Error: archivo no encontrado: {e.filename}")
except Exception as e:
    print("Error al combinar archivos:", e)