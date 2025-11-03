try:
    nombre = input("Nombre: ").strip()
    edad = input("Edad: ").strip()
    carrera = input("Carrera: ").strip()

    with open("perfil.txt", "w", encoding="utf-8") as f:
        f.write(f"{nombre}\n")
        f.write(f"{edad}\n")
        f.write(f"{carrera}\n")

    print("Datos guardados en 'perfil.txt'.")
except Exception as e:
    print("Error al guardar el archivo:", e)
```try:
    nombre = input("Nombre: ").strip()
    edad = input("Edad: ").strip()
    carrera = input("Carrera: ").strip()

    with open("perfil.txt", "w", encoding="utf-8") as f:
        f.write(f"{nombre}\n")
        f.write(f"{edad}\n")
        f.write(f"{carrera}\n")

    print("Datos guardados en 'perfil.txt'.")
except Exception as e:
    print("Error al guardar el archivo:", e)