import requests

url = "https://pokeapi.co/api/v2/pokemon/25"

try:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    nombre = data.get("name", "N/A")
    tipos = [t["type"]["name"] for t in data.get("types", [])]

    print(f"Nombre: {nombre}")
    print("Tipos:", ", ".join(tipos) if tipos else "N/A")
except requests.RequestException as e:
    print("Error en la petición:", e)
except ValueError:
    print("Respuesta no es JSON válido.")
```import requests

url = "https://pokeapi.co/api/v2/pokemon/25"

try:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    nombre = data.get("name", "N/A")
    tipos = [t["type"]["name"] for t in data.get("types", [])]

    print(f"Nombre: {nombre}")
    print("Tipos:", ", ".join(tipos) if tipos else "N/A")
except requests.RequestException as e:
    print("Error en la petición:", e)
except ValueError:
    print("Respuesta no es JSON válido.")