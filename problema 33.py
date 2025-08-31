nombre = input("Introduce el nombre del vendedor: ")
ventas = float(input("Introduce el volumen de ventas en pesos: "))

if ventas < 1000:
    situacion = "Despedido"
elif 1000 <= ventas < 5000:
    situacion = "En periodo de prueba"
elif 5000 <= ventas < 10000:
    situacion = "Bono del 5%"
else:
    situacion = "Bono del 10%"

print(f"{nombre}: {situacion}")