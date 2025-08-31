producto = input("Introduce el nombre del producto: ")
precio_sin_iva = float(input("Introduce el precio sin IVA: "))
iva = precio_sin_iva * 0.16
precio_con_iva = precio_sin_iva + iva
print(f"El producto '{producto}' tiene un precio final con IVA de {precio_con_iva:.2f} pesos.")