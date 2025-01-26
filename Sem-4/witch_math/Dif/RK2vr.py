import numpy as np

def f(x0, y0, n, h, func):
    x = [x0]
    y = [y0]
    for i in range(n):
        y_half = np.round(y[i] + h/2 * func(x[i], y[i]), 10)
        y_new = np.round(y[i] + h * func(x[i] + h/2, y_half), 10)
        
        x.append(x[i] + h)
        y.append(y_new)
        print(f'{i}. {x[-1]} {y[-1]}')
        
        print(f'__\ny{i+1/2} = {y_half}')
        print(f'y{i+1} = {y_new}\n')
    return x[-1], y[-1]
        

def func(x, y):
    return np.array([y[1], (x * np.exp(x) + y[0] + y[1]) / 3])

x0 = 0
y0 = np.array([2, 1])
h = 0.2
n = 3

print(f(x0, y0, n, h, func))