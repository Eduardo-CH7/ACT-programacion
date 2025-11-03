
import os

carpeta = input("Introduce el nombre (o ruta) de la carpeta: ").strip()

if not os.path.isdir(carpeta):
    print("Error: la carpeta no existe.")
else:
    archivos = [f for f in sorted(os.listdir(carpeta)) 
                if f.lower().endswith(".csv") and os.path.isfile(os.path.join(carpeta, f))]
    if archivos:
        print("Archivos .csv encontrados:")
        for a in archivos:
            print(a)
    else:
        print("No se encontraron archivos .csv en la carpeta.")
```
import os

carpeta = input("Introduce el nombre (o ruta) de la carpeta: ").strip()

if not os.path.isdir(carpeta):
    print("Error: la carpeta no existe.")
else:
    archivos = [f for f in sorted(os.listdir(carpeta)) 
                if f.lower().endswith(".csv") and os.path.isfile(os.path.join(carpeta, f))]
    if archivos:
        print("Archivos .csv encontrados:")
        for a in archivos:
            print(a)
    else:
        print("No se encontraron archivos .csv en la carpeta.")