try:
    frase = input("Introduce una frase para agregar al registro: ")
    with open("registro.txt", "a", encoding="utf-8") as f:
        f.write(frase + "\n")
    print("Frase agregada a 'registro.txt'.")
except Exception as e:
    print("Error al escribir en el archivo:", e)