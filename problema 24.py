capital_inicial = float(input("Introduce el capital inicial: "))
tasa_interes = float(input("Introduce la tasa de interés anual (en %): "))
periodos = int(input("Introduce el número de periodos (años): "))

# Interés simple
interes_simple = capital_inicial * (1 + (tasa_interes / 100) * periodos)

# Interés compuesto
interes_compuesto = capital_inicial * ((1 + (tasa_interes / 100)) ** periodos)

print(f"Capital final con interés simple: {interes_simple:.2f}")
print(f"Capital final con interés compuesto: {interes_compuesto:.2f}")