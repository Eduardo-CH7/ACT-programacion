import sys
import os

def main():
    if len(sys.argv) != 3:
        print("Uso: python lector.py <archivo.txt> <n>")
        sys.exit(1)

    archivo = sys.argv[1]
    try:
        n = int(sys.argv[2])
        if n < 0:
            raise ValueError
    except ValueError:
        print("Error: el segundo argumento debe ser un número entero no negativo.")
        sys.exit(1)

    if not os.path.isfile(archivo):
        print(f"Error: el archivo '{archivo}' no existe.")
        sys.exit(1)

    try:
        with open(archivo, "r", encoding="utf-8") as f:
            for i, linea in enumerate(f):
                if i >= n:
                    break
                print(linea.rstrip("\n"))
    except Exception as e:
        print("Error al leer el archivo:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()