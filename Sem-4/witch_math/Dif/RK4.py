import numpy as np

def f(x0, y0, n, h, func):
    x = [x0]
    y = [y0]
    
    for i in range(0, n):
        k1 = np.round(func(x[i],y[i]), 10)
        k2 = np.round(func(x[i] + h/2, y[i] + h/2 * k1), 10)
        k3 = np.round(func(x[i] + h / 2, y[i] + h / 2 * k2), 10)
        k4 = np.round(func(x[i] + h, y[i] + h * k3),10)

        y_new = y[i] + h/6 * (k1 + 2 * k2 + 2 * k3 + k4)
        
        x.append(round(x[i] + h, 10))
        y.append(np.round(y_new, 10))

        print(f'{i}. {x[-1]} {y[-1]}')


        # print(f"Step {i}:")
        # print(f"k1: {k1}")
        # print(f"k2: {k2}")
        # print(f"k3: {k3}")
        # print(f"k4: {k4}")
        # print(f"y_{i + 1}:", np.round(y_new, 5))
        # print()
        
    return x[-1], y[-1]
        
def func(x, y):
    return np.array([y[1], (x * np.exp(x) + y[0] + y[1]) / 3])

x0 = 0
y0 = np.array([2, 1])
h = 0.2
n = 5

print(f(x0, y0, n, h, func))
# y = f(x0, y0, n, h, func)
# for i in range(len(y)):
#     print(i, y[i])