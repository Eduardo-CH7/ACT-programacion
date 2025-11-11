import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=19.43&longitude=-99.13&current_weather=true"

try:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    current = data.get("current_weather")
    if not current:
        print("No se encontró 'current_weather' en la respuesta.")
    else:
        temperatura = current.get("temperature")
        velocidad_viento = current.get("windspeed")

        if temperatura is not None:
            print(f"Temperatura actual: {temperatura} °C")
        else:
            print("Temperatura no disponible.")

        if velocidad_viento is not None:
            print(f"Velocidad del viento: {velocidad_viento}")
        else:
            print("Velocidad del viento no disponible.")

except requests.RequestException as e:
    print("Error en la petición:", e)
except ValueError:
    print("Respuesta no es JSON válido.")
```import requests

url = "https://api.open-meteo.com/v1/forecast?latitude=19.43&longitude=-99.13&current_weather=true"

try:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    current = data.get("current_weather")
    if not current:
        print("No se encontró 'current_weather' en la respuesta.")
    else:
        temperatura = current.get("temperature")
        velocidad_viento = current.get("windspeed")

        if temperatura is not None:
            print(f"Temperatura actual: {temperatura} °C")
        else:
            print("Temperatura no disponible.")

        if velocidad_viento is not None:
            print(f"Velocidad del viento: {velocidad_viento}")
        else:
            print("Velocidad del viento no disponible.")

except requests.RequestException as e:
    print("Error en la petición:", e)
except ValueError:
    print("Respuesta no es JSON válido.")