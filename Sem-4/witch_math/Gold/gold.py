from scipy import optimize
import matplotlib.pyplot as plt

a = 0
b = 8
eps = 10**-5
coef = 0.618

def f(t):
    return t**2 - 10*t


def main():
    opt(a, b, eps)
    solution = optimize.minimize_scalar(f)
    print(f'\nРеальный минимум:\nx = {solution.x}\nf(x)min = {solution.fun}')

def opt(a, b, eps):
    it = 1
    x2 = round(a + coef * (b-a), 6)
    x1 = round(b - coef * (b-a), 6)
    while (abs(x2 - x1) > eps):
        print(f'{it:>2}. a = {a:>8} x1 = {x1:>8} x2 = {x2:>8} b = {b:>8}')
        f_old = f(x2)
        if (f(x1) > f_old):
            a = x1
            x1 = x2
            x2 = round(a + coef * (b-a), 6)
            f_old = f(x2)
        else:
            b = x2
            x2 = x1
            x1 = round(b - coef * (b-a), 6)
            f_old = f(x1)
        it += 1
    x = (a + b) / 2
    print(f'\nx = {x}\nf(x)min = {f(x)}')    
    

if __name__ == '__main__':
    main()