horas_extra = int(input("Introduce la cantidad de horas extra trabajadas: "))

salario_normal = 40 * 63
salario_extra = horas_extra * 80
salario_total = salario_normal + salario_extra

print(f"El salario semanal total es: {salario_total} pesos.")