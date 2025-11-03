import matplotlib.pyplot as plt

x = [1, 2, 3, 4, 5]
y = [2, 4, 1, 8, 7]

plt.figure()
plt.plot(x, y, 'o-', color='tab:blue', linewidth=2, markersize=6) 
plt.title("Gráfica de x vs y")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.tight_layout()

plt.savefig("grafica.png")  
plt.show()