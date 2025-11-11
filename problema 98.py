import requests

word = input("Introduce la palabra en inglés: ").strip()
url = f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}"

try:
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    data = resp.json()

    entrada = data[0]
    palabra = entrada.get("word", word)

    
    definicion = None
    for meaning in entrada.get("meanings", []):
        defs = meaning.get("definitions", [])
        if defs:
            definicion = defs[0].get("definition")
            if definicion:
                break

    if definicion:
        print(f"Palabra: {palabra}")
        print(f"Definición principal: {definicion}")
    else:
        print("No se encontró una definición válida en la respuesta.")

except requests.exceptions.HTTPError:
    print("Error: la API no encontró la palabra o respondió con error HTTP.")
except requests.exceptions.RequestException as e:
    print("Error en la petición:", e)
except (ValueError, IndexError, KeyError):
    print("Error procesando la respuesta JSON.")