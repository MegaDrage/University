def print_matrix(matrix, v_nums):
    n = len(matrix)
    for i in range(0,n):
        for j in range(0,n):
            print( f"{matrix[i][j]:>7.3f}", end=' ')
        print(f'| {v_nums[i]:>7.3f}', end='\n')

def print_ans(x):
    print('\n')
    for i in range(len(x)):
        print(f'x{i} = {x[i]:>7.3f}')


def gauss_method(A, b):
    n = len(A)
    print_matrix(A, b)
    for k in range(n - 1):
        for i in range(k+1, n):
            mult = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= mult * A[k][j]
            b[i] -= mult * b[k]
        print(mult)
        print_matrix(A, b)
    x = [0] * n
    for i in range(n-1, -1, -1):
        s = b[i]
        for j in range(i+1, n):
            s -= A[i][j] * x[j]
        x[i] = s / A[i][i]
    
    return x

def gauss_method_mod(A, b):
    n = len(A)
    
    for k in range(n):
        max_row = k
        for i in range(k+1, n):
            if abs(A[i][k]) > abs(A[max_row][k]):
                max_row = i
        A[k], A[max_row] = A[max_row], A[k]
        b[k], b[max_row] = b[max_row], b[k]
        
        for i in range(k+1, n):
            mult = A[i][k] / A[k][k]
            for j in range(k, n):
                A[i][j] -= mult * A[k][j]
            b[i] -= mult * b[k]
                        
    x = [0] * n
    for i in range(n-1, -1, -1):
        s = b[i]
        for j in range(i+1, n):
            s -= A[i][j] * x[j]
        x[i] = s / A[i][i]
    
    return x

with open('input.txt', 'r') as file:
    n = int(file.readline().strip())
    A = []
    b = []
    for i in range(n):
        row = [float(x) for x in file.readline().strip().split()]
        A.append(row[:-1])
        b.append(float(row[-1]))

x = gauss_method(A, b)
print_ans(x)
print_matrix(A, b)