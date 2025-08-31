edad = int(input("Introduce tu edad: "))

if edad < 0 or edad > 120:
    clasificacion = "Edad inválida"
elif edad < 10:
    clasificacion = "Niño"
elif 10 <= edad <= 17:
    clasificacion = "Adolescente"
elif 18 <= edad <= 29:
    clasificacion = "Joven"
elif 30 <= edad <= 59:
    clasificacion = "Adulto"
else:
    clasificacion = "Adulto mayor"

print(f"Clasificación: {clasificacion}")

if 18 <= edad <= 120:
    print("Eres mayor de edad.")
else:
    print("No eres mayor de edad.")