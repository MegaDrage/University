import math
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

def f(x, y, z):
    F = [0.0, 0.0]
    F[0] = np.sin(z) + np.sin(np.exp(x)) + np.sin(y) + y
    F[1] = np.exp(x) + 3 * np.sin(np.exp(x))
    return F

def runge_kutta4(a, b, h, y, z, flag=False):
    n = round((b - a) / h) + 1
    X = [a + i * h for i in range(n)]
    Y = [y, z]
    if flag:
        print(f"x = {X[0]:.4f}, y = {Y[0]:.12f}, y' = {Y[1]:.12f}")
    for i in range(1, n):
        K1 = f(X[i-1], Y[0], Y[1])
        K2 = f(X[i-1] + h / 2, Y[0] + h / 2 * K1[0], Y[1] + h / 2 * K1[1])
        K3 = f(X[i-1] + h / 2, Y[0] + h / 2 * K2[0], Y[1] + h / 2 * K2[1])
        K4 = f(X[i-1] + h, Y[0] + h * K3[0], Y[1] + h * K3[1])
        Y[0] += h / 6 * (K1[0] + 2 * K2[0] + 2 * K3[0] + K4[0])
        Y[1] += h / 6 * (K1[1] + 2 * K2[1] + 2 * K3[1] + K4[1])
        if flag:
            print(f"x = {X[i]:.4f}, y = {Y[0]:.12f}, y' = {Y[1]:.12f}")
    return Y

def runge_kutta4_o(a, b, h, y, z, flag=False):
    n = round((b - a) / h) + 1
    X = [a + i * h for i in range(n)]
    Y = [y, z]
    Z = [z]
    if flag:
        print(f"x = {X[0]:.4f}, y = {Y[0]:.12f}, y' = {Y[1]:.12f}")
    for i in range(1, n):
        K1 = f(X[i-1], Y[0], Y[1])
        K2 = f(X[i-1] + h / 2, Y[0] + h / 2 * K1[0], Y[1] + h / 2 * K1[1])
        K3 = f(X[i-1] + h / 2, Y[0] + h / 2 * K2[0], Y[1] + h / 2 * K2[1])
        K4 = f(X[i-1] + h, Y[0] + h * K3[0], Y[1] + h * K3[1])
        Y[0] += h / 6 * (K1[0] + 2 * K2[0] + 2 * K3[0] + K4[0])
        Y[1] += h / 6 * (K1[1] + 2 * K2[1] + 2 * K3[1] + K4[1])
        Z.append(Y[1])
        if flag:
            print(f"x = {X[i]:.4f}, y = {Y[0]:.12f}, y' = {Y[1]:.12f}")
    return X, Z

def runge_kutta4_i(a, b, h, y0, z0, flag=False):
    n = round((b - a) / h) + 1
    X = [a + i * h for i in range(n)]
    Y = [y0]
    Z = [z0]
    if flag:
        print(f"x = {X[0]:.4f}, y = {Y[0]:.12f}, z = {Z[0]:.12f}")
    for i in range(1, n):
        K1 = f(X[i-1], Y[i-1], Z[i-1])
        K2 = f(X[i-1] + h / 2, Y[i-1] + h / 2 * K1[0], Z[i-1] + h / 2 * K1[1])
        K3 = f(X[i-1] + h / 2, Y[i-1] + h / 2 * K2[0], Z[i-1] + h / 2 * K2[1])
        K4 = f(X[i-1] + h, Y[i-1] + h * K3[0], Z[i-1] + h * K3[1])
        Y.append(Y[i-1] + h / 6 * (K1[0] + 2 * K2[0] + 2 * K3[0] + K4[0]))
        Z.append(Z[i-1] + h / 6 * (K1[1] + 2 * K2[1] + 2 * K3[1] + K4[1]))
        if flag:
            print(f"x = {X[i]:.4f}, y = {Y[i]:.12f}, z = {Z[i]:.12f}")
    return X, Y, Z
def prist(eps, h, a, b, y0, y1):
    if b - a == 0:
        raise ValueError("Interval length (b - a) cannot be zero.")
    
    # Improved initial guesses for the derivative using a higher-order approximation
    angle = [-(y1-y0)/(b-a), (y1-y0)/(b-a)]
    angle[0] *= 0.5  # Adjust the first guess
    angle[1] *= 1.5  # Adjust the second guess
    print(f"Initial guesses for derivative: {angle}")
    
    exp = runge_kutta4(a, b, h, y0, angle[0], False)
    other_exp = runge_kutta4(a, b, h, y0, angle[1], False)
    
    if any(np.isnan(exp)) or any(np.isnan(other_exp)):
        raise ValueError("Runge-Kutta integration returned NaN values.")
    
    s3 = angle[1]
    Es1 = exp[1] - y1
    Es2 = other_exp[1] - y1
    
    print(f"Initial errors: Es1 = {Es1}, Es2 = {Es2}")
    
    while abs(s3) >= eps:
        Es_dif = Es1 - Es2
        if Es_dif == 0:
            print("Difference in errors (Es_dif) is zero, breaking loop.")
            break
        
        s3 = angle[1] - Es2 * (angle[0] - angle[1]) / Es_dif
        print(f"Updated derivative guess: s3 = {s3}")
        
        exp = runge_kutta4(a, b, h, y0, s3, False)
        
        if any(np.isnan(exp)):
            raise ValueError("Runge-Kutta integration returned NaN values.")
        
        Es1 = exp[1] - y1
        print(f"Updated error: Es1 = {Es1}")
        
        angle[0] = angle[1]
        angle[1] = exp[1]
        Es2 = Es1
    
    # Check if the final derivative guess is close to the expected value
    expected_derivative = np.exp(1)
    if abs(s3 - expected_derivative) > eps:
        print(f"Warning: Final derivative guess {s3} is not close to the expected value {expected_derivative}.")
    
    return s3

def dv_peresch(eps, h, a, b, y0, y1):
    Y1 = runge_kutta4(a, b, h, y0, y1, False)
    Y2 = runge_kutta4(a, b, h / 2, y0, y1, False)
    while abs(Y1[0] - Y2[0]) > eps:
        h /= 2
        Y1 = Y2
        Y2 = runge_kutta4(a, b, h / 2, y0, y1, False)
    print('-' * 20)
    print(f'h = {h / 2}')
    return h / 2


def main():
    p = 2
    
    h = 0.1
    eps = h ** (p + 6)
    
    x0 = 0
    x1 = 1
    
    
    y0 = 1
    y1 = np.exp(1)
    
    angle = prist(eps, h, x0, x1, y0, y1)
    h_new = dv_peresch(eps, h, x0, x1, y0, -angle)
    angle = prist(eps, h_new, x0, x1, y0, y1)
    Y = runge_kutta4(x0, x1, h_new, y0, -angle, True)

if __name__ == "__main__":
    main()
