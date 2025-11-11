import requests

url = "https://pokeapi.co/api/v2/pokemon?limit=5"
try:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()
    for item in data.get("results", []):
        print(item.get("name", "N/A"))
except requests.RequestException as e:
    print("Error en la petición:", e)
except ValueError:
    print("Respuesta no es JSON válido.")