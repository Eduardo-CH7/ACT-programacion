
try:
    with open("numeros.txt", "r", encoding="utf-8") as f:
        total = 0.0
        cuenta = 0
        for num_linea, linea in enumerate(f, 1):
            texto = linea.strip()
            if texto == "":
                continue
            try:
                valor = float(texto)
            except ValueError:
                print(f"Línea {num_linea} no es un número válido ('{texto}') — se omite")
                continue
            total += valor
            cuenta += 1

    try:
        promedio = total / cuenta
    except ZeroDivisionError:
        print("No hay números válidos en 'numeros.txt' para calcular el promedio.")
    else:
        print(f"Promedio: {promedio:.6f}")
except FileNotFoundError:
    print("Error: el archivo 'numeros.txt' no existe.")
except Exception as e:
    print("Error inesperado:", e)
```
try:
    with open("numeros.txt", "r", encoding="utf-8") as f:
        total = 0.0
        cuenta = 0
        for num_linea, linea in enumerate(f, 1):
            texto = linea.strip()
            if texto == "":
                continue
            try:
                valor = float(texto)
            except ValueError:
                print(f"Línea {num_linea} no es un número válido ('{texto}') — se omite")
                continue
            total += valor
            cuenta += 1

    try:
        promedio = total / cuenta
    except ZeroDivisionError:
        print("No hay números válidos en 'numeros.txt' para calcular el promedio.")
    else:
        print(f"Promedio: {promedio:.6f}")
except FileNotFoundError:
    print("Error: el archivo 'numeros.txt' no existe.")
except Exception as e:
    print("Error inesperado:", e)