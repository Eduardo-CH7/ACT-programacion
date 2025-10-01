def factorial(n):
    if n < 0:
        return "No existe factorial para números negativos"
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

def pedir_numeros_y_mostrar_factorial():
    contador = 0
    while True:
        entrada = input("Introduce un número (o escribe 'fin' para terminar): ")
        if entrada.lower() == "fin":
            break
        try:
            numero = int(entrada)
            print(f"El factorial de {numero} es: {factorial(numero)}")
            contador += 1
        except ValueError:
            print("Por favor, introduce un número válido o 'fin' para salir.")
    print(f"Cantidad total de números leídos: {contador}")