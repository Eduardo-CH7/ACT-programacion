try:
    nombre = input("Introduce el nombre del archivo: ").strip()
    with open(nombre, "r", encoding="utf-8") as f:
        contenido = f.read(5)

    if len(contenido) < 5:
        raise EOFError

    numero = int(contenido)
except FileNotFoundError:
    print(f"Error: el archivo '{nombre}' no existe.")
except EOFError:
    print("Error: el archivo tiene menos de 5 caracteres.")
except ValueError:
    print("Error: los primeros 5 caracteres no se pueden convertir a entero.")
except Exception as e:
    print("Error inesperado:", e)
else:
    print(f"Entero obtenido: {numero}")