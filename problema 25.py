x1 = float(input("Introduce x₁: "))
y1 = float(input("Introduce y₁: "))
x2 = float(input("Introduce x₂: "))
y2 = float(input("Introduce y₂: "))

if x2 != x1:
    pendiente = (y2 - y1) / (x2 - x1)
    b = y1 - pendiente * x1
    print(f"La pendiente (m) es: {pendiente:.2f}")
    print(f"La ecuación de la recta es: y = {pendiente:.2f}x + {b:.2f}")
else:
    print("La pendiente es indefinida (recta vertical).")