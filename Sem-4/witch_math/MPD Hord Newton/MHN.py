def f(x):
    return x**2 - 3

def f_p(x):
    return 2*x

def mpd(a, b, eps):
    i = 1
    while abs(b-a)/2 > eps:
        c = (a+b)/2
        print(f"{i})  C = {c}")
        first = f(a)*f(c)
        sec = f(c)*f(b)
        if first<0:
            b = c
        elif sec < 0:
            a = c
        i += 1

def hord(a, b, eps):
    c = a
    c_prev = b
    i = 1
    delta = c_prev - c
    while abs(delta) > eps:
        c_prev = c
        c = (a*f(b)-b*f(a))/(f(b)-f(a))
        print(f"{i})  C = {c}")
        first = f(a)*f(c)
        sec = f(c)*f(b)
        if first < 0:
            b = c
        elif sec < 0:
            a = c
        i += 1
        delta = c_prev - c



def Newton(a, b, eps):
    if f(a) > 0:
        x = a
    elif f(b) > 0:
        x = b
    i = 0
    x_prev = x
    while True:
        x = x - f(x)/f_p(x)
        print(f"X{i+1} = {x}")
        if abs(x_prev - x) < eps:
            break

        else:
            i+=1
            x_prev = x



def main():
    a, b = 1, 2
    eps = 10**-6

    print("МПД\n")
    mpd(a, b, eps)
    print("\n\nМетод хорд\n")
    hord(a, b, eps)
    print("\n\nМетод Ньютона\n")
    Newton(a, b, eps)



if __name__ == "__main__":
    main()