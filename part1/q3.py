import numpy as np
import matplotlib.pyplot as plt

def ode_function(r, N, B):
    return -2 * N / r + 2 / (3 * r) - 4 * B * r**3 / 3

def calculate_step_size(r0, end_r, num_steps):
    return (end_r - r0) / num_steps

def euler_method(ode_func, r0, N0, B, h, end_r):
    r_values = [r0]
    N_values = [N0]
    r = r0
    N = N0
    while r < end_r:
        N += h * ode_func(r, N, B)
        r += h
        r_values.append(r)
        N_values.append(N)
    return np.array(r_values), np.array(N_values)

def rk(ode_func, r0, N0, B, h, end_r):
    r_values = [r0]
    N_values = [N0]
    r = r0
    N = N0
    while r < end_r:
        k1 = h * ode_func(r, N, B)
        k2 = h * ode_func(r + h/2, N + k1/2, B)
        k3 = h * ode_func(r + h/2, N + k2/2, B)
        k4 = h * ode_func(r + h, N + k3, B)
        N += (k1 + 2*k2 + 2*k3 + k4) / 6
        r += h
        r_values.append(r)
        N_values.append(N)
    return np.array(r_values), np.array(N_values)

# User inputs
B = float(input("Enter the value for B: "))
r0 = float(input("Enter the initial value for r: "))
N0 = float(input("Enter the initial value for N: "))
num_steps = int(input("Enter the number of steps: "))
end_r = float(input("Enter the end value for r: "))

h = calculate_step_size(r0, end_r, num_steps)

r_euler, N_euler = euler_method(ode_function, r0, N0, B, h, end_r)
r_rk4, N_rk4 = rk(ode_function, r0, N0, B, h, end_r)

# Plot the solutions
plt.figure(figsize=(10, 6))
plt.plot(r_euler, N_euler, label="Euler Method")
plt.plot(r_rk4, N_rk4, label="Runge-Kutta (RK) Method 4th Order")
plt.title("Solution of the ODE")
plt.xlabel("r")
plt.ylabel("N")
plt.legend()
plt.grid(True)
plt.show()
