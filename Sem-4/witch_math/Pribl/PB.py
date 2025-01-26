import math

class NwI:
    def __init__(self, main=None, accur=None):
        if (main != None and accur!= None):
            self.main = main
            self.accur = accur
        if (main == None and accur== None):
            self.main = 0
            self.accur = 0

    def __add__(self, other):
        s = sum(self, other)
        return s

    def __sub__(self, other):
        d = dif(self, other)
        return d

    def __truediv__(self, other):
        d = div(self, other)
        return d

    def __mul__(self, other):
        m = mult(self, other)
        return m

    def __pow__(self, power, modulo=None):
        if power < 1 and power > 0:
            p = root(self, power)
        else:
            p = deg(self, power)
        return p



def main():
    x = NwI(1.3534, 0.022)
    y = NwI(2.0874, 0.014)

    print("\n")
    a3 = (y**2+xdegy(x,y))/(root(y,2)+y)
    printNI(a3)
    
    


def printNI(a):
    print(a.main, u"\u00B1", a.accur, "\n")


def sum(x, y):
    osn = x.main + y.main
    pogr = x.accur + y.accur
    res = NwI(round(osn, 3), round(pogr, 3))
    print("x + y =", end=' ')
    printNI(res)
    return res


def dif(x, y):
    osn = x.main - y.main
    pogr = x.accur + y.accur
    res = NwI(round(osn, 3), round(pogr, 3))
    print("x - y =", end=' ')
    printNI(res)
    return res


def mult(x, y):
    a1 = NwI(1, round(x.accur/x.main,3))
    b1 = NwI(1, round(y.accur/y.main,3))
    c = x.main*y.main
    c1 = NwI(1, round(a1.accur+b1.accur,3))
    res = NwI(round(c,3), round(c*c1.accur,3))
    print("x * y =", end=' ')
    printNI(res)
    return res


def div(x, y):
    a1 = NwI(1, abs(round(x.accur / x.main, 3)))
    b1 = NwI(1, abs(round(y.accur / y.main, 3)))
    c = x.main / y.main
    c1 = NwI(1, round(a1.accur + b1.accur, 3))
    res = NwI(round(c * c1.main, 3), abs(round(c * c1.accur, 3)))
    print("x / y =", end=' ')
    printNI(res)
    return res


def deg(x = None, deg = None):
    if x != None and deg == None:
        deg = 2
    a = x.main
    a1 = NwI(1, round(deg * x.accur / x.main, 3))
    c = x.main ** deg
    c1 = NwI(1, round(a1.accur, 3))
    res = NwI(round(c * c1.main, 3), round(c * c1.accur, 3))
    print(f"x^{deg:<3} =", end=' ')
    printNI(res)
    return res


def root(x, deg):
    if x != None and deg == None:
        deg = 2
    a = x.main**(1./deg)
    a1 = NwI(1, round(x.accur/(deg*x.main), 3))
    res = NwI(round(a * a1.main, 3), round(a * a1.accur, 3))
    print(f"{deg}\u221ax =", end=' ')
    printNI(res)
    return res


def ln(x):
    a = math.log(x.main)
    a1 = round(1/x.main, 3)
    a2 = round(x.accur,3)
    res = NwI(round(a,3), round(a1 * a2,3))
    print("ln(x) = ", end=' ')
    printNI(res)
    return res


def xdegy(x, y):
    l = ln(x)
    deg = mult(l,y)
    res = e(deg)
    print("x^y = ", end=' ')
    printNI(res)
    return res


def e(x):
    res = NwI(round(math.exp(x.main),3), round(math.exp(x.main)*x.accur, 3))

    return res

def sin(x):
    a=math.sin(x.main)
    a1=math.cos(x.main)
    res = NwI(round(a,3), abs(round(a1*x.accur, 3)))
    print("sin(X) = ", end=" ")
    printNI(res)
    return res

def cos(x):
    a=math.cos(x.main)
    a1=math.sin(x.main)
    res = NwI(round(a,3), abs(round(a1*x.accur, 3)))
    print("cos(X) = ", end=" ")
    printNI(res)
    return res

def tg(x):
    res = sin(x)/cos(x)
    print("tg(x) =", end=' ')
    printNI(res)
    return res

if __name__ == '__main__':
    main()