import math

def MPI(B, C, N):
    X = [0,0,0]
    i = 0
    while i < N:
        X = subtract(B, mult(C, X))
        print(f"X{i+1}", end='')
        print_vector(X)
        print(' ')
        i+=1


def Zeidel(B, C, eps):
    X = [0,0,0]
    X_prev = [10000,10000,10000]
    i = 0
    delta = X_prev[1]-X[1]
    while abs(delta)>eps:
        X_prev[1] = X[1]
        for j in range(len(X)):
            s = sum(C[j][k] * X[k] for k in range(len(X)) if k != j)
            X[j] = B[j] - s
        print(f"X{i+1}", end='')
        print_vector(X)
        print(' ')
        i+=1
        delta = X_prev[1]-X[1]


def main():
    nums, l, v_nums, lv = readfiles()
    nums = tofloat(nums)
    v_nums = tofloat(v_nums)
    
    if math.sqrt(l) % 1 != 0:
        print('Не получится построить квадратную матрицу')
        exit()
    if int(math.sqrt(l)) != lv:
        print('Количество свободных членов не совпадает с количеством переменных')
        exit()
    
    else:
        n = int(math.sqrt(l))
        eps = 0.001
        A = init(n, nums)
        print_matrix(A, v_nums)
        A_div, B = div(A, v_nums)
        E, C = separate(A_div)
        print('\nE:', end='')
        print_matrix(E)
        print('C:', end='')
        print_matrix(C)
        print('B:', end='')
        print_vector(B)
        N = count_N(C, B, eps)
        print('МПИ:')
        MPI(B,C,N)
        print('Метод Зейделя:')
        Zeidel(B,C,eps)
        
        



def count_N(C,B,eps):
    end_C, end_B = endless(C,B)
    N = math.ceil((math.log((eps*(1-end_C))/end_B)/(math.log(end_C)))+1)
    print(f"\n{N}\n\n")
    return N

def subtract(A, B):
    res = [0]*len(A)
    for i in range(len(A)):
        res[i] = round(A[i] - B[i], 6)
    return res

def mult(A,B):
    res_rows = len(B)
    res = [0]*res_rows
    for i in range(len(A)):
        for j in range(len(A[0])):
            res[i] += round(A[i][j]*B[j], 7)
    return res

def endless(C, B):
    max_C = 0
    max_B = 0
    for i in range(len(C)):
        if sum(C[i]) > max_C:
            max_C = sum(C[i])
    max_B = max(B) 
    return max_C, max_B

def div(A, v_nums):
    for i in range(len(A)):
        divider = A[i][i]
        for j in range(len(A)):
            A[i][j] = round(A[i][j] / divider, 5)
        v_nums[i] = round(v_nums[i] / divider, 5)
    print_matrix(A, v_nums)
    return A, v_nums

def separate(A):
    n = len(A)
    E = [0]*n
    for i in range(n):
        E[i] = [0]*n
    C = A
    for i in range(n):
        E[i][i] = 1
        C[i][i] = 0
    return E, C
    

def tofloat(list):
    for i in range(len(list)):
        list[i] = float(list[i])
    return list

def readfiles():
    with open('matrix_mpi.txt','r') as f:
        nums = f.readlines()
        l = len(nums)
        if l == 1:
            nums = nums[0].split(' ')
            l = len(nums)
    
    with open('vector_mpi.txt','r') as fv:
        vetor_nums = fv.readlines()
        lv = len(vetor_nums)
        if lv == 1:
            vetor_nums = vetor_nums[0].split(' ')
            lv = len(vetor_nums)
    
    return nums, l, vetor_nums, lv

def init(n, nums):
    matrix = [0]*n
    for i in range(n):
        matrix[i] = [0]*n
    k=0
    for i in range(0,n):
        for j in range(0,n):
            matrix[i][j] = nums[k]
            k+=1
    return matrix

def print_matrix(matrix=None, v_nums=None):
    if matrix != None and v_nums != None:
        n = len(matrix)
        print('')
        for i in range(0,n):
            for j in range(0,n):
                print( f"{matrix[i][j]:>7.3f}", end=' ')
            print(f'| {v_nums[i]:>7.3f}', end='\n')
    
    if matrix != None and v_nums == None:
        n = len(matrix)
        print('')
        for i in range(0,n):
            for j in range(0,n):
                print( f"{matrix[i][j]:>7.3f}", end=' ')
            print('')

def print_vector(vector):
    n = len(vector)
    print('')
    for i in range(n):
        if vector[i] < 0.0000001:
            print(f'{abs(vector[i]):>7.5f}', end='\n')
        else:
            print(f'{vector[i]:>7.5f}', end='\n')


if __name__ == '__main__':
    main()