import requests

num = input("Introduce un número: ").strip()
try:
    int(num)
except ValueError:
    print("Entrada no válida: debe ser un número entero.")
else:
    url = f"https://numbersapi.com/{num}?json"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        print(data.get("text", "No se encontró trivia para ese número."))
    except requests.RequestException as e:
        print("Error en la petición:", e)
    except ValueError:
        print("Error: la respuesta no es JSON válido.")
import requests

num = input("Introduce un número: ").strip()
try:
    int(num)
except ValueError:
    print("Entrada no válida: debe ser un número entero.")
else:
    url = f"https://numbersapi.com/{num}?json"
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        data = resp.json()
        print(data.get("text", "No se encontró trivia para ese número."))
    except requests.RequestException as e:
        print("Error en la petición:", e)
    except ValueError:
        print("Error: la respuesta no es JSON válido.")