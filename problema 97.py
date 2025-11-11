import requests
import json

url = "https://numbersapi.com/42?json"  

try:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    with open("respuesta.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Respuesta guardada en 'respuesta.json'.")
except requests.RequestException as e:
    print("Error en la petición:", e)
except ValueError:
    print("Error: la respuesta no es JSON válido.")
```import requests
import json

url = "https://numbersapi.com/42?json"  

try:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    with open("respuesta.json", "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)

    print("Respuesta guardada en 'respuesta.json'.")
except requests.RequestException as e:
    print("Error en la petición:", e)
except ValueError:
    print("Error: la respuesta no es JSON válido.")