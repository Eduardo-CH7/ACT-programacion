while True:
    capital = float(input("Introduce el capital inicial (C): "))
    tasa = float(input("Introduce la tasa de interés (i, en decimal, por ejemplo 0.05 para 5%): "))
    periodos = int(input("Introduce el número de periodos (n): "))

    monto = capital * (1 + tasa) ** periodos
    print(f"El monto final (M) es: {monto:.2f}")

    repetir = input("¿Deseas calcular otro interés compuesto? (sí/no): ").strip().lower()
    if repetir != "sí":
        break