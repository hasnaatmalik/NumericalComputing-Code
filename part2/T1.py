import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Read data from the file
data = np.genfromtxt('bps.dat')

# Split data into x, y, z
x = data[:, 0]
y = data[:, 1]
z = data[:, 2]

# Perform cubic spline interpolation
cs = CubicSpline(x, z)

# Generate points for plotting
x_plot = np.linspace(min(x), max(x), 1000)
z_plot = cs(x_plot)

# Plot the graph
plt.figure(figsize=(10, 6))
plt.plot(x, z, 'o', label='Data Points')
plt.plot(x_plot, z_plot, '-', label='Cubic Spline Interpolation')
plt.xlabel('x')
plt.ylabel('z')
plt.title('Cubic Spline Interpolation')
plt.legend()
plt.grid(True)
plt.show()
