import sympy as sp
def newtonRaphson(func, x0, tol=0.0001, maxIterations=100):
    x = sp.symbols('x')
    f = func
    f_prime = sp.diff(f, x)
    x_n = x0
    iterations = 0
    while iterations < maxIterations:
        f_val = f.subs(x, x_n)
        if abs(f_val) < tol:
            break

        f_prime_val = f_prime.subs(x, x_n)
        if f_prime_val == 0:
            print("Derivative is zero")
            return None

        x_n = x_n - f_val / f_prime_val
        iterations += 1

    if iterations == maxIterations:
        print("Maximum iterations reached, No convergence.")
        return None
    return round(x_n, 4)

def initialGuess(func, start, end, step=1):
    x = sp.symbols('x')
    f = func

    x_val = start
    prev_sign = sp.sign(f.subs(x, x_val))
    while x_val <= end:
        x_val += step
        curr_sign = sp.sign(f.subs(x, x_val))

        if curr_sign != prev_sign:
            return x_val - step

        prev_sign = curr_sign
    print("No sign change found in the given range.")
    return None

# Get user input for the equation
equation_str = input("Enter the equation in terms of 'x': ")
x = sp.symbols('x')
equation = sp.sympify(equation_str)

# Get user input for the range
start = float(input("Enter the start of the range: "))
end = float(input("Enter the end of the range: "))

initial_guess = initialGuess(equation, start, end)
print(f"Initial guess for {equation}: {initial_guess}")

root1 = newtonRaphson(equation, initial_guess)
if root1 is not None:
    print("Root is:", root1)
