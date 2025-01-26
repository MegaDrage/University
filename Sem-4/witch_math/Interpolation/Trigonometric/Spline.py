import Gauss
import matplotlib.pyplot as plt

def main():
    global x
    x,y = init()
    print(x, y, "\n")
    C,d = find_C(x,y)
    for i in range(len(C)):
        print(C[i])
    print("\n",d)
    M = Gauss.gauss_method(C,d)
    M = [0] + M + [0]
    S = find_s(x,y,M,1.1)
    graph(x,y,M)


def h(i):
    return x[i]-x[i-1]   

def graph(x,y,m):
    plt.plot(x, y)
    x_r = [0]*(int(x[-1])*10-19)
    y_r = [0]*(int(x[-1])*10-19)
    for i in range(20, int(x[-1])*10+1):
        x_r[i-20] = i/10
        y_r[i-20] = find_s(x, y, m, i/10)
    plt.plot(x_r, y_r)
    plt.show()
    


def find_s(x,y,M, point):
    s = 0
    i = 0
    for k in range(len(x)):
        if x[k] > point:
            i = k
            break
    s += M[i-1]*((x[i]-point)**3)/(6*h(i))
    s += M[i]*((point-x[i-1])**3)/(6*h(i))
    s += (y[i-1] - (M[i-1]*(h(i))**2)/6)*((x[i]-point)/h(i))
    s += (y[i] - (M[i]*(h(i))**2)/6)*((point-x[i-1])/h(i))
    return s
    
    
def find_C(x,y):
    C = [0] * (len(x))
    d = [0] * (len(x) - 2)
    for i in range(len(x)):
        C[i] = [0] * (len(x) - 1)
    
    for i in range(1, len(x) - 1):
        for j in range(1, len(x)):
            if i == j:
                C[i][j-1] = (h(i)+h(i+1))/3
            elif j == i + 1:
                C[i][j-1] = h(i+1)/6
            elif j == i - 1:
                C[i][j-1] = h(i)/6
            elif abs(j-1) > 1:
                C[i][j-1] = 0
    for i in range(1,len(y)-1):
        d[i-1] = ((y[i+1]-y[i])/(h(i+1))) - ((y[i]-y[i-1])/(h(i)))
    return C[1:-1],d

def init():
    with open("nums.txt", "r") as f:
        nums = f.readlines()
        n = len(nums)
        x = [0] * n
        y = [0] * n
        for i in range(n):
            raw = nums[i].split()
            x[i] = float(raw[0])
            y[i] = float(raw[1])
    return x, y


if __name__ == "__main__":
    main()