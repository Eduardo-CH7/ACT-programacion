import math

num1 = float(input("Introduce el primer número: "))
num2 = float(input("Introduce el segundo número: "))

suma = num1 + num2
resta = num1 - num2
multiplicacion = num1 * num2
division = num1 / num2 if num2 != 0 else "No se puede dividir entre cero"
potenciacion = num1 ** num2
raiz_cuadrada = math.sqrt(num1) if num1 >= 0 else "No se puede calcular la raíz cuadrada de un número negativo"
modulo = num1 % num2 if num2 != 0 else "No se puede calcular el módulo con divisor cero"

print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicación: {multiplicacion}")
print(f"División: {division}")
print(f"Potenciación: {potenciacion}")
print(f"Raíz cuadrada del primero: {raiz_cuadrada}")
print(f"Módulo: {modulo}")