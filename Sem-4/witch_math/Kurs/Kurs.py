import math
import numpy as np
import matplotlib.pyplot as plt

def f(x, y, z):
    F = [0.0, 0.0]
    F[0] = z
    F[1] = (math.exp(x) + y + z) / 3
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

def runge_kutta2(a, b, h, y, z, flag=False):
    n = round((b - a) / h) + 1
    X = [a + i * h for i in range(n)]
    Y = [y, z]
    if flag:
        print(f"x = {X[0]:.4f}, y = {Y[0]:.12f}, y' = {Y[1]:.12f}")
    for i in range(1, n):
        K1 = f(X[i-1], Y[0], Y[1])
        K2 = f(X[i-1] + h / 2, Y[0] + h / 2 * K1[0], Y[1] + h / 2 * K1[1])
        Y[0] += h * K2[0]
        Y[1] += h * K2[1]
        if flag:
            print(f"x = {X[i]:.4f}, y = {Y[0]:.12f}, y' = {Y[1]:.12f}")
    return Y

def prist(eps, h, a, b, y0, y1):
    angle = [(y1-y0)/(b - a), (y1-y0)/(b - a)]
    exp = runge_kutta4(a, b, h, y0, angle[0], False)
    if exp[0] < y1:
        while exp[0] < y1:
            angle[1] += 1
            exp = runge_kutta4(a, b, h, y0, angle[1], False)
    elif exp[0] > y1:
        while exp[0] > y1:
            angle[1] -= 1
            exp = runge_kutta4(a, b, h, y0, angle[1], False)
    if angle[0] > angle[1]:
        angle[0], angle[1] = angle[1], angle[0]

    left = angle[0]
    right = angle[1]
    midle = (left + right) / 2
    exp = runge_kutta4(a, b, h, y0, midle, False)

    while abs(exp[0] - y1) > eps:
        if exp[0] < y1:
            left = midle
        elif exp[0] > y1:
            right = midle
        midle = (left + right) / 2
        exp = runge_kutta4(a, b, h, y0, midle, False)
    return midle

def dv_peresch(eps, h, a, b, y0, y1, p, flag):
    if flag:
        if p == 2:
            Y1 = runge_kutta2(a, b, h, y0, y1, True)
            Y2 = runge_kutta2(a, b, h / 2, y0, y1, True)
            while abs(Y1[0] - Y2[0]) > eps:
                print(f'h = {h / 2}')
                h /= 2
                Y1 = Y2
                Y2 = runge_kutta2(a, b, h / 2, y0, y1, True)
        if p == 4:
            Y1 = runge_kutta4(a, b, h, y0, y1, True)
            Y2 = runge_kutta4(a, b, h / 2, y0, y1, True)
            while abs(Y1[0] - Y2[0]) > eps:
                print(f'h = {h / 2}')
                h /= 2
                Y1 = Y2
                Y2 = runge_kutta4(a, b, h / 2, y0, y1, True)
    else:
        Y1 = runge_kutta4(a, b, h, y0, y1, False)
        Y2 = runge_kutta4(a, b, h / 2, y0, y1, False)
        while abs(Y1[0] - Y2[0]) > eps:
            h /= 2
            Y1 = Y2
            Y2 = runge_kutta4(a, b, h / 2, y0, y1, False)
        print('-' * 20)
        print(f'h = {h / 2}')
    return h / 2

def plot_solution(a, b, h, y0, z0, method=runge_kutta4):
    n = round((b - a) / h) + 1
    X = [a + i * h for i in range(n)]
    Y = [y0]
    Z = [z0]
    for i in range(1, n):
        K1 = f(X[i-1], Y[i-1], Z[i-1])
        K2 = f(X[i-1] + h / 2, Y[i-1] + h / 2 * K1[0], Z[i-1] + h / 2 * K1[1])
        K3 = f(X[i-1] + h / 2, Y[i-1] + h / 2 * K2[0], Z[i-1] + h / 2 * K2[1])
        K4 = f(X[i-1] + h, Y[i-1] + h * K3[0], Z[i-1] + h * K3[1])
        Y.append(Y[i-1] + h / 6 * (K1[0] + 2 * K2[0] + 2 * K3[0] + K4[0]))
        Z.append(Z[i-1] + h / 6 * (K1[1] + 2 * K2[1] + 2 * K3[1] + K4[1]))
    plt.plot(X, Y, label='y(x)')
    plt.plot(X, Z, label="y'(x)")
    plt.xlabel('x')
    plt.ylabel('y, y\'')
    plt.title('Решение уравнения')
    plt.legend()
    plt.grid(True)
    plt.show()


def main():
    p = 0
    
    h = 0.1
    eps = h ** (p + 6)
    
    a = 0
    b = 1
    
    yb = 1
    
    y0 = 1
    y1 = 3
    

    # if p == 2 or p == 4:
    #     print(f'Last h = {dv_peresch(eps, h, a, b, y0, yb, p, True)}')
    # else:
    angle = prist(eps, h, a, b, y0, y1)
    h_new = dv_peresch(eps, h, a, b, y0, angle, p, False)
    angle = prist(eps, h_new, a, b, y0, y1)
    Y = runge_kutta4(a, b, h_new, y0, angle, True)

    print(h_new)

if __name__ == "__main__":
    main()
