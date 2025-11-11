import requests

try:
    resp = requests.get("https://numbersapi.com/42?json", timeout=10)
    resp.raise_for_status()
    data = resp.json()
    print(data.get("text", "Campo 'text' no encontrado en la respuesta."))
except requests.exceptions.RequestException as e:
    print("Error en la petición:", e)
except ValueError:
    print("Respuesta no es JSON válido.")