from tabulate import tabulate

def InputMatrix():
    m = int(input("Enter number of rows in matrix 1: "))
    n = int(input("Enter number of columns in matrix 1 = number of rows in matrix 2: "))
    k = int(input("Enter number of columns in matrix 2: "))
    M1 = list()
    M2 = list()
    for i in range(m):
        R = list(map(int, input(f"Enter row {i+1} of Matrix 1: ").split()))
        assert(len(R) == n), "Invalid number of elements"
        M1.append(R)
    print("Matrix 1 saved successfuly")
    print(tabulate(M1))
    for j in range(n):
        R = list(map(int, input(f"Enter row {j+1} of Matrix 2: ").split()))
        assert(len(R) == k), "Invalid number of elements"
        M2.append(R)
    print("Matrix 2 saved successfuly")
    print(tabulate(M2))
    return M1, M2

def Multiply(M1, M2):
    assert(len(M1[0]) == len(M2)), "Invalid Matrices for multiplication"
    M=list()
    m = len(M1)
    n = len(M2[0])
    l = len(M1[0])
    for i in range(m):
        M.append([0]*n)
    for i in range(m):
        for j in range(n):
            S = 0
            for k in range(l):
                S += M1[i][k]*M2[k][j]
            M[i][j] = S
    print("Final Multiplication Product: ")
    print(tabulate(M))

if __name__ == "__main__":
    M1, M2 = InputMatrix()
    Multiply(M1, M2)
