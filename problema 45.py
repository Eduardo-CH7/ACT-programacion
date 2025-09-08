while True:
    print("\nCalculadora básica")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Exponente")
    print("6. Módulo (residuo)")

    opcion = input("Elige una opción (1-6): ")

    if opcion not in ["1", "2", "3", "4", "5", "6"]:
        print("Opción no válida.")
        continue

    repetir_operacion = True
    while repetir_operacion:
        num1 = float(input("Introduce el primer número: "))
        num2 = float(input("Introduce el segundo número: "))

        if opcion == "1":
            resultado = num1 + num2
            print(f"Resultado: {resultado}")
        elif opcion == "2":
            resultado = num1 - num2
            print(f"Resultado: {resultado}")
        elif opcion == "3":
            resultado = num1 * num2
            print(f"Resultado: {resultado}")
        elif opcion == "4":
            if num2 == 0:
                print("Error: No se puede dividir entre cero.")
            else:
                resultado = num1 / num2
                print(f"Resultado: {resultado}")
        elif opcion == "5":
            resultado = num1 ** num2
            print(f"Resultado: {resultado}")
        elif opcion == "6":
            if num2 == 0:
                print("Error: No se puede calcular el módulo con divisor cero.")
            else:
                resultado = num1 % num2
                print(f"Resultado: {resultado}")

        repetir = input("¿Deseas repetir la misma operación? (sí/no): ").strip().lower()
        if repetir != "sí":
            repetir_operacion = False

    otra = input("¿Deseas realizar otra operación distinta? (sí/no): ").strip().lower()
    if otra != "sí":
        break