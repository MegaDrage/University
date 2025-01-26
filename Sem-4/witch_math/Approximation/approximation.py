import Gauss
import matplotlib.pyplot as plt
import math

x0 = 1
i_start = 0
i_end = 3
h = 0.1
n = i_end - i_start + 1
alph = ['a', 'b', 'c', 'd', 'e']

def g0(x):
    return 1

def g1(x):
    return x

def g2(x):
    return math.sqrt(x)

def f(x):
    return x**2
funcs = [g0, g1, g2]

def main():
    x = init()
    c = C(funcs, x)
    D = d(funcs, x)
    a = Gauss.gauss_method(c, D)
    print('Коэффициенты:')
    for i in range(len(a)):
        print(f'{alph[i]} = {a[i]}') 
    graph(x, funcs, a)
    
def graph(x, funcs, a):
    y = [0] * n
    gg = [0] * n * 100
    xx = [0] * n * 100
    for i in range(n):
        y[i] = f(x[i])
    
    for i in range(1, (n * 100)+1):
        xx[i-1] = x0 + (i-1)*h/100
        gg[i-1] = g(funcs, a, xx[i-1])
    
    plt.scatter(x,y, fc = 'none', ec='r')
    plt.plot(xx,gg,'b--')
    plt.show()
    

def g(f, a, x):
    gg = 0
    for i in range(len(a)):
        gg += a[i] * f[i](x)
    return gg
    
def C(g, x):
    C = [0] * len(funcs)
    for i in range(len(g)):
        C[i] = [0] * len(g)
    
    for p in range(len(g)):
        for j in range(len(g)):
            for i in range(n):
                C[p][j] += g[j](x[i]) * g[p](x[i])        
    return C

def d(g, x):
    d = [0] * len(g)
    for p in range(len(g)):
        for i in range(n):
            d[p] += f(x[i]) * g[p](x[i])
    return d        

def init():
    x = [0] * (n)
    for i in range(n):
        x[i] = x0 + h * i
    return x


if __name__ == '__main__':
    main()