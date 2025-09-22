productos = []
precios = []
ventas = []

for i in range(5):
    nombre = input(f"Nombre del producto {i+1}: ")
    precio = float(input(f"Precio de {nombre}: "))
    venta = int(input(f"Volumen de ventas de {nombre}: "))
    productos.append(nombre)
    precios.append(precio)
    ventas.append(venta)

print("\nReporte de productos:")
print("Producto\tPrecio\tVentas\tIngreso")
for i in range(5):
    ingreso = precios[i] * ventas[i]
    print(f"{productos[i]}\t{precios[i]:.2f}\t{ventas[i]}\t{ingreso:.2f}")