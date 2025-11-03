from numpy import sin
from scipy.integrate import quad

resultado, error = quad(lambda x: sin(x**2), 0, 2)
print(f"Integral de sin(x^2) en [0, 2] = {resultado:.6f} (error estimado: {error:.2e})")
```from numpy import sin
from scipy.integrate import quad

resultado, error = quad(lambda x: sin(x**2), 0, 2)
print(f"Integral de sin(x^2) en [0, 2] = {resultado:.6f} (error estimado: {error:.2e})")