import numpy as np
import matplotlib.pyplot as plt

# Titik data
x = np.array([5, 10, 15, 20, 25, 30, 35, 40])
y = np.array([40, 30, 25, 40, 18, 22, 15, 10])

# Interpolasi Lagrange
def lagrange_interpolation(x_values, y_values, x):
    def L(k, x):
        term = 1
        for i in range(len(x_values)):
            if i != k:
                term *= (x - x_values[i]) / (x_values[k] - x_values[i])
        return term
    
    P = 0
    for k in range(len(y_values)):
        P += y_values[k] * L(k, x)
    return P

# Interpolasi Newton
def newton_interpolation(x_values, y_values, x):
    n = len(x_values)
    divided_diff = np.zeros((n, n))
    divided_diff[:,0] = y_values
    
    for j in range(1, n):
        for i in range(n - j):
            divided_diff[i,j] = (divided_diff[i+1,j-1] - divided_diff[i,j-1]) / (x_values[i+j] - x_values[i])
    
    def N(x):
        result = divided_diff[0,0]
        product = 1.0
        for i in range(1, n):
            product *= (x - x_values[i-1])
            result += divided_diff[0,i] * product
        return result
    
    return N(x)

# Menghasilkan titik interpolasi
x_interp = np.linspace(5, 40, 100)
y_lagrange = [lagrange_interpolation(x, y, xi) for xi in x_interp]
y_newton = [newton_interpolation(x, y, xi) for xi in x_interp]

# Memplot hasil
plt.figure(figsize=(12, 6))
plt.plot(x, y, 'o', label='Titik Data')
plt.plot(x_interp, y_lagrange, '-', label='Interpolasi Lagrange')
plt.plot(x_interp, y_newton, '--', label='Interpolasi Newton')
plt.xlabel('Tegangan, x (kg/mm^2)')
plt.ylabel('Waktu patah, y (jam)')
plt.legend()
plt.title('Interpolasi Lagrange dan Newton')
plt.grid(True)
plt.show()
