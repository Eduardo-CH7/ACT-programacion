import requests

try:
    resp = requests.get("https://api.github.com", timeout=10)
    print("Status code:", resp.status_code)
    if resp.status_code == 200:
        print("Todo bien")
except requests.RequestException as e:
    print("Error en la petición:", e)