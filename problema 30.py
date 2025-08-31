precio_unitario = float(input("Introduce el precio unitario del producto: "))
cantidad_vendida = int(input("Introduce la cantidad vendida: "))
egresos = float(input("Introduce el total de egresos de la empresa: "))

ingresos = precio_unitario * cantidad_vendida

if ingresos < egresos:
    print("La empresa está en pérdidas (ingresos < egresos).")
elif ingresos == egresos:
    print("La empresa está en punto de equilibrio (ingresos = egresos).")
else:
    print("La empresa está generando ganancias (ingresos > egresos).")