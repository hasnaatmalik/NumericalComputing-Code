import numpy as np
def runge_kutta(f, g, x0, y0, z0, h):
    k1 = h * f(x0, y0, z0)
    l1 = h * g(x0, y0, z0)
    k2 = h * f(x0 + 0.5 * h, y0 + 0.5 * k1, z0 + 0.5 * l1)
    l2 = h * g(x0 + 0.5 * h, y0 + 0.5 * k1, z0 + 0.5 * l1)
    k3 = h * f(x0 + 0.5 * h, y0 + 0.5 * k2, z0 + 0.5 * l2)
    l3 = h * g(x0 + 0.5 * h, y0 + 0.5 * k2, z0 + 0.5 * l2)
    k4 = h * f(x0 + h, y0 + k3, z0 + l3)
    l4 = h * g(x0 + h, y0 + k3, z0 + l3)
    x_next = x0 + h
    y_next = y0 + (k1 + 2 * k2 + 2 * k3 + k4) / 6
    z_next = z0 + (l1 + 2 * l2 + 2 * l3 + l4) / 6
    return x_next, y_next, z_next
 
def f(x, y, z):
    return (y*z)+x
 
def g(x, y, z):
    return (x*z)+y

x0 = 0
y0 = 1
z0 = -1
h_step = 0.2
x_final = 1
x_points = np.arange(x0, x_final + h_step, h_step)
 
solPoints = [(x0, y0, z0)]
for x in x_points[1:]:
    next_x, next_y, next_z = runge_kutta(f, g, solPoints[-1][0], solPoints[-1][1], solPoints[-1][2], h_step)
    solPoints.append((next_x, next_y, next_z))
 

print("Solution Given Below:")
for x, y, z in solPoints:
    print(f"At x = {x:.2f}, y = {y:.4f}, z = {z:.4f}")