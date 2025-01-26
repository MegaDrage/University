from sympy import *
import numpy as np
import Gauss

x0 = np.array([3.0, 1.0])

x,y = symbols('x y')
f1 = x**2 + y**2 - 13
f2 = x*y - 4
foo = [f1, f2]
var = ['x', 'y']

def Newton_inv_matrix(x0, eps):
    i = 1
    print("Метод с обратной матрицей:")
    while true:
        W = pr(x0)
        W_inv = np.linalg.inv(W)
        x1 = x0 - np.dot(W_inv, F(x0))
        print(f'#{i}: x = {x1[0]} y = {x1[1]}')
        r = x1 - x0
        for j in range(len(r)):
            r[j] = float(r[j])
        if np.linalg.norm(r) < eps:
            break
        x0 = x1  
        i+=1   
        
        
def Newton_SLAU(x0, eps):
    print("\nМетод с решением СЛАУ:")
    i = 1
    while True:
        f = F(x0)
        w = pr(x0)
        X = Gauss.gauss_method(w, f)
        x1 = x0 - X
        print(f'#{i}: x = {x1[0]} y = {x1[1]}')
        if abs(x1[0] - x0[0]) < eps and abs(x1[1] - x0[1]) < eps:
            break
        x0 = x1
        i += 1
        
    
    
def main():
    Newton_inv_matrix(x0, 0.000001)
    Newton_SLAU(x0, 0.000001)
    
    
def F(x0 = None):
    f = [0] * len(foo)
    if x0.all() == None:
        for i in range(len(f)):
            f[i] = foo[i]
    else:
        for i in range(len(x0)):
            f[i] = foo[i].subs([(x, x0[0]), (y, x0[1])])
    return f
    
def pr(f = None):
    der = [0] * len(foo)
    for i in range(len(foo)):
        der[i] = [0]*len(var)
    for i in range(len(foo)):
        for j in range(len(var)):
            der[i][j] = foo[i].diff(var[j])
            
    if f.all() == None:
        return der
    
    else:
        for i in range(len(foo)):
            for j in range(len(var)):
                der[i][j] = int(der[i][j].subs([(x, f[0]), (y, f[1])]))
        return der
        
    

def print_m(f):
    for i in range(len(f)):
        print(f[i])
    print('')

def Sqrt(x):
  return np.sqrt(np.double(x))

if __name__ == '__main__':
    main()