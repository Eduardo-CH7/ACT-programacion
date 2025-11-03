import sympy as sp

x = sp.symbols('x')


eq1 = sp.Eq(x**2 - 5*x + 7, 0)
sol1 = sp.solve(eq1, x)


eq2 = sp.Eq(7*x**2 + 9*x - 7, 8*x**2 - 2*x - 3)
sol2 = sp.solve(eq2, x)

print("a) Ecuación:", eq1)
print("   Soluciones simbólicas:", sol1)

print("\nb) Ecuación:", eq2)
print("   Soluciones simbólicas:", sol2)
```import sympy as sp

x = sp.symbols('x')


eq1 = sp.Eq(x**2 - 5*x + 7, 0)
sol1 = sp.solve(eq1, x)


eq2 = sp.Eq(7*x**2 + 9*x - 7, 8*x**2 - 2*x - 3)
sol2 = sp.solve(eq2, x)

print("a) Ecuación:", eq1)