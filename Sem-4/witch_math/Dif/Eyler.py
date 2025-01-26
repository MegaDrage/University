import numpy as np

def f(x0, y0, n, h, func):
    x = [x0]
    y = [y0]
    it = 1
    for i in range(0, n):
        x.append(round(x[i] + h, 10))
        y_new = np.round(y[i] + h * func(x[i], y[i]), 10)
        y.append(y_new)
        print(f'{it}. {x[-1]} {y[-1]}')
        it += 1
    return x[-1], y[-1]
      
def func(x, y):
    return np.array([y[1], (x * np.exp(x) + y[0] + y[1]) / 3])
    

x0 = 0
y0 = np.array([2, 1])
h = 0.2
n = 10

print(f(x0, y0, n, h, func))