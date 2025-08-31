precio_venta = float(input("Introduce el precio de venta por pieza: "))
cantidad_vendida = int(input("Introduce la cantidad vendida: "))
costo_fijo = float(input("Introduce el costo fijo: "))
costo_variable = float(input("Introduce el costo variable por pieza: "))

ingresos = precio_venta * cantidad_vendida
costos_totales = costo_fijo + (costo_variable * cantidad_vendida)
beneficio = ingresos - costos_totales

print(f"El beneficio total es: {beneficio:.2f} pesos.")