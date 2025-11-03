try:
    with open("entrada.txt", "r", encoding="utf-8") as f:
        for num, linea in enumerate(f, 1):
            print(f"{num}: {linea.rstrip()}")
except FileNotFoundError:
    print("Error: el archivo 'entrada.txt' no existe.")
```
try:
    with open("entrada.txt", "r", encoding="utf-8") as f:
        for num, linea in enumerate(f, 1):
            print(f"{num}: {linea.rstrip()}")
except FileNotFoundError:
    print("Error: el archivo 'entrada.txt' no existe.")