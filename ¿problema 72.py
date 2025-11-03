import pandas as pd

data = {
    "Producto": ["bimbo", "alpura", "suavitel", "pachoncito"],
    "Precio": [45, 27, 72, 103],
    "Cantidad": [400, 350, 273, 321]
}

df = pd.DataFrame(data)

print("DataFrame:")
print(df)

print("\nEstadísticos principales:")

print(df.describe(include="all"))