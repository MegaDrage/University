import matplotlib.pyplot as plt
import math

data = [2.56]

def main():
    x, y = init()
    
    # for num in data:
        # print(f"Лагранж для {num} : {Lagrange(x, y, num)}")
        # print(f"Эйткен для {num} : {Eytken(x, y, len(x)-1, num)}")
        # print(f"1 формула Ньютона для {num} : {newton_1(num, x,y)}")
        # print(f"2 формула Ньютона для {num} : {newton_2(num, x, y)}\n")
        # print(f"Обратная интерполяция для {num}: {Lagrange(y,x,num)}\n")
        
    graph(x,y)


def print_tabl(x,y,delta):
    print('{:>10}'.format('x'), end=' ')
    print('{:>10}'.format('y'), end=' ')
    for k in range(len(delta)):
        print("{:>10}".format('Δ^'+str(k+1)+'y'), end=' ')
    print('\n'+'-'*10*(len(delta)+3))    
    for i in range(len(delta)):
        print(f"{x[i]:>10.3}", end=' ')
        print(f"{y[i]:>10.3}", end=' ')
        for j in range(len(delta[i])):
            if delta[i][j] == None:
                delta[i][j] = 0.0
            print(f"{delta[i][j]:>10.3}", end=' ')
        print(' ')
    print('\n')
    
    
def divided_differences(x, y, k):
    n = len(x)
    F = [[None] * n for _ in range(n)]
    for i in range(n):
        F[i][0] = y[i]
    for j in range(1, n):
        for i in range(n - j):
            F[i][j] = (F[i + 1][j - 1] - F[i][j - 1]) / (x[i + j] - x[i])
    #print_tabl(x, y, F)
    if k == 1:
        return F[0]
    if k == 2:
        F_2 = [0] * n
        for i in range(n):
            for j in range(n):
                if i + j == n-1:
                    F_2[i] = F[i][j]
        return F_2
        

def newton_1(point, x, y):
    F = divided_differences(x, y, 1)
    n = len(x)
    res = F[0]
    for i in range(1, n):
        q = F[i]
        for j in range(i):
            q *= ((point - x[0]) - j)
        res += q
    return round(res, 5)


def newton_2(point, x, y):
    F = divided_differences(x, y, 2)
    F.reverse()
    n = len(x)
    res = F[0]
    for i in range(1, n):
        q = F[i]
        for j in range(i):
            q *= ((point - x[n-1]) + j)
        res += q
    return round(res, 5)
    
    
def Lagrange(x, y, point):
    n = len(x)
    res = 0.0
    for i in range(n):
        g = y[i]
        for j in range(n):
            if j != i:
                g *= (point - x[j])/(x[i] - x[j])
        res += g
    return round(res, 5)    
    

def Eytken(x, y, n, point):
    m = n
    P = y[0:n+1]
    for j in range(m):
        for i in range(m): 
            if i + j + 1 <= n:
                P[i] = (P[i]*(point - x[i+j+1]) - P[i+1]*(point - x[i]))/(x[i] - x[i+j+1])
        m -= 1     
    return round(P[0], 5)    
       

    
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
                
                
def graph(x,y):
    x_r = [0]*(int(x[-1])*10)
    y_r = [0]*(int(x[-1])*10)
    x_e = x_l = x_n1 = x_n2 = x
    y_e = y_l = y_n1 = y_n2= y
    # for i in range(int(x[-1])*10):
    #     x_r[i] = (i+1)/10
    #     y_r[i] = math.sin((i+1)/10)
    
    for i in range(int(x[-1])*10):
        x_r[i] = (i+1)/10
        y_r[i] = math.sqrt((i+1)/10)
    
    for k in range(len(data)):
        for i in range(1,len(x)):
            if x[i] > data[k]:
                y_l = y_l[0:i] + [Lagrange(x_l, y_l, data[k])] + y_l[i:]
                print(y_l)
                x_l = x_l[0:i] + [data[k]] + x_l[i:]
                print(x_l)
                
                y_e = y_e[0:i] + [Eytken(x_e, y_e, len(x_e)-1, data[k])] + y_e[i:]
                x_e = x_e[0:i] + [data[k]] + x_e[i:]
                
                y_n1 = y_n1[0:i] + [newton_1(data[k], x_l, y_l)] + y_n1[i:]
                x_n1 = x_n1[0:i] + [data[k]] + x_n1[i:]
                
                y_n2 = y_n2[0:i] + [newton_2(data[k], x_n2, y_n2)] + y_n2[i:]
                x_n2 = x_n2[0:i] + [data[k]] + x_n2[i:]
                break
                
    figure, axis = plt.subplots(2, 2) 
    figure.set_size_inches(10,10)
    axis[0][0].plot(x_l,y_l,"b", linewidth=2.0)
    axis[0][0].plot(x_l,y_l,"bo", linewidth=2.0)
    axis[0][0].plot(x_r,y_r,"r--", linewidth=2.0)
    axis[0, 0].set_title("Лагранж") 
    
    axis[0][1].plot(x_e,y_e,"y", linewidth=2.0)
    axis[0][1].plot(x_e,y_e,"yo", linewidth=2.0)
    axis[0][1].plot(x_r,y_r,"r--", linewidth=2.0)
    axis[0, 1].set_title("Эйткен") 
    
    axis[1][0].plot(x_n1,y_n1,"g", linewidth=2.0)
    axis[1][0].plot(x_n1,y_n1,"go", linewidth=2.0)
    axis[1][0].plot(x_r,y_r,"r--", linewidth=2.0)
    axis[1, 0].set_title("Ньютон 1") 
    
    axis[1][1].plot(x_n2,y_n2, "c", linewidth=2.0)
    axis[1][1].plot(x_n2,y_n2, "co", linewidth=2.0)
    axis[1][1].plot(x_r,y_r,"r--", linewidth=2.0)
    axis[1, 1].set_title("Ньютон 2") 
    plt.show()

    

if __name__ == "__main__":
    main()
