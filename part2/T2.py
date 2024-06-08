import sympy as sp

# Define symbols
x, y, z, r, m, q = sp.symbols('x y z r m q')

# Define equations
eq1 = 1 - (2 * m / r) + (3 * m * q / r**3) - x**2 * r**2
eq2 = 1 / (1 - (2 * m / r) + (3 * m * q**2 / r**3)) - y**2 / (x + z * r)**2
# Derivative of the second equation with respect to r
eq3 = sp.diff(eq2, r)

# Substitute given values for m, q, and r
eq1 = eq1.subs({m: 1, q: 1, r: 1})
eq2 = eq2.subs({m: 1, q: 1, r: 1})
eq3 = eq3.subs({m: 1, q: 1, r: 1})

# Solve equations
solutions = sp.solve((eq1, eq2, eq3), (x, y, z))

# Print solutions
print("Solutions:")
for sol in solutions:
    x_val = sol[0].evalf()
    y_val = sol[1].evalf()
    z_val = sol[2].evalf()
    print("x =", x_val)
    print("y =", y_val)
    print("z =", z_val)
    break
