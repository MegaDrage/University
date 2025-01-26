import numpy as np
import matplotlib.pyplot as plt

point = 1.5
x0 = 1
h = 1
n = 6
coef = 10

def main():
    
    x,y = init(x0, h, n)
    print(f"{x}\n{y}")
    print(find_y(point, y))
    graph(x,y)

def graph(x, y):
    s = [0] * int((n) * coef)
    i = 0
    re = [0] * int((n) * coef)
    im = [0] * int((n) * coef)
    y_orig = [0] * int((n) * coef)
    for i in range(len(s)):
        s[i] = round((x[0] + 1 * (h/2) + h*i) / coef, 4)
        xx = find_y(s[i], y)
        re[i] = xx.real
        im[i] = xx.imag
        y_orig[i] = func(s[i])
        print(s[i], y_orig[i])
        
    plt.plot(x,y,'ro', label='points')
    plt.plot(s,re,'b', label='real')
    plt.plot(s,im,'g', label='imaginary')

    x_func = np.linspace(x[0], x[-1], 1000)
    y_func = func(x_func)
    plt.plot(x_func, y_func, 'k', label='func(x)')

    plt.legend()
    plt.show()
        
        

def func(x):
    return 1/x
    
def init(x0, h, n):
    x = [0] * n
    y = [0] * n
    for i in range(n):
        x[i] = x0 + i * h
        y[i] = func(x[i])
    return x,y

def A(j, y):
    a = 0
    i = 1j
    for k in range(n):
        a += y[k] * (np.cos(-2 * np.pi * (k*j)/n) + i * np.sin(-2 * np.pi * (k*j)/n))
        #print(y[k], round(np.cos(-2 * np.pi * (k*j)/n), 4) + i * round(np.sin(-2 * np.pi * (k*j)/n), 4))
        
    return a
    
def find_y(x, y):
    yx = 0
    i = 1j
    if n % 2 == 0:
        for j in range(int(-n/2)+1, int(n/2)+1):
            yx += A(j,y) * (np.cos(2*np.pi*j*(x-x0)/(n*h)) + i * np.sin(2*np.pi*j*(x-x0)/(n*h)))
    else:
        for j in range(int(-n/2), int(n/2)+1):
            yx += A(j,y) * (np.cos(2*np.pi*j*(x-x0)/(n*h)) + i * np.sin(2*np.pi*j*(x-x0)/(n*h)))
    yx *= 1/n
    return np.round(yx, 4)
    

if __name__ == "__main__":
    main()