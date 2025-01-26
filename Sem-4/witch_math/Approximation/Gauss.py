import math

def tofloat(list):
    for i in range(len(list)):
        list[i] = float(list[i])
    return list
    

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

def print_matrix(matrix, v_nums):
    n = len(matrix)
    for i in range(0,n):
        for j in range(0,n):
            print( f"{matrix[i][j]:>7.3f}", end=' ')
        print(f'| {v_nums[i]:>7.3f}', end='\n')
        
def gauss_method(matrix, vector):
    n = len(matrix)
    for i in range(n):
        max_el = abs(matrix[i][i])
        max_row = i
        for k in range(i + 1, n):
            if abs(matrix[k][i]) > max_el:
                max_el = abs(matrix[k][i])
                max_row = k

        matrix[i], matrix[max_row] = matrix[max_row], matrix[i]
        vector[i], vector[max_row] = vector[max_row], vector[i]

        for k in range(i + 1, n):
            c = -matrix[k][i] / matrix[i][i]
            for j in range(i, n):
                if i == j:
                    matrix[k][j] = 0
                else:
                    matrix[k][j] += c * matrix[i][j]
            vector[k] += c * vector[i]
    
    #print('\n')
    #print_matrix(matrix, vector)
    
    x = [0 for _ in range(n)]
    for i in range(n - 1, -1, -1):
        x[i] = vector[i] / matrix[i][i]
        for k in range(i - 1, -1, -1):
            vector[k] -= matrix[k][i] * x[i]
    return x


def print_ans(x):
    print('\n')
    for i in range(len(x)):
        print(f'x{i} = {x[i]:>7.3f}')
        
