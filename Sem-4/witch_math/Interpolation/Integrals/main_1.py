import numpy as np 

eps = 10**-8

def f(x): 
    return 1/x

def func_trapezoide(a, b, h, last=None):
    n = int((b - a) / h) 
    x = np.linspace(a, b, n + 1) 
    y = f(x)
    integral_trapezoidal = (h / 2) * (y[0] + 2 * np.sum(y[1:n]) + y[n])
    if last is not None:
        diff = abs(integral_trapezoidal - last)
    else:
        diff = None
    print("step:", h, "Интеграл: ", integral_trapezoidal, "Погрешность: ", diff)
    return integral_trapezoidal, diff

def func_simpson(a, b, h, last=None):
    n = int((b - a) / h) 
    x = np.linspace(a, b, n + 1) 
    y = f(x)
    integral_simpson = (h / 3) * (y[0] + 4 * np.sum(y[1:n:2]) + 2 * np.sum(y[2:n-1:2]) + y[n]) 
    if last is not None:
        diff = abs(integral_simpson - last)
    else:
        diff = None
    print("step:", h, "Интеграл: ", integral_simpson, "Погрешность: ", diff)
    return integral_simpson, diff

a = 1 
b = 2  
h = 0.1
last_val = None

print("Трапеция")
while True:
    val, diff = func_trapezoide(a, b, h, last_val)
    if last_val is not None and diff is not None and diff < eps:
        break
    last_val = val
    h /= 2

print("Погрешность: ", diff)

a = 1 
b = 2  
h = 0.1
last_val = None

print("Симпсон")
while True:
    val, diff = func_simpson(a, b, h, last_val)
    if last_val is not None and diff is not None and diff < eps:
        break
    last_val = val
    h /= 2

print("Погрешность: ", diff)