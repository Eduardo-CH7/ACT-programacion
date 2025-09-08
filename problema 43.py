total = 0

while total <= 100000:
    abono = float(input("¿Cantidad a abonar? "))
    if abono < 0:
        print("Error: No se aceptan cantidades negativas.")
        continue
    total += abono

print(f"¡Meta alcanzada! El total abonado es: ${total:.2f}")