import copy
def MatrixMultiply(M1: list, M2: list) -> list :
    assert len(M1[0]) == len(M2), "Inavlid matrices for multiplication"
    M = [[0]*len(M2[0]) for _ in range(len(M1))]
    for i in range(len(M1)):
        for j in range(len(M2[0])):
            S = 0
            for k in range(len(M2)):
                S += M1[i][k]*M2[k][j]
            M[i][j] = S
    return M

if __name__ == "__main__":
    L = list(map(int, input("Enter matrix elements separated by a space: ").split()))
    R= int(input("Enter no. of rows/columns for the square matrix: "))
    assert (len(L) == R*R), "Invalid Elements of Dimensions"
    M = [L[i: i+R] for i in range(0, len(L), R)]
    print("Original Matrix: ")
    for row in M:
        print(row)
    n = int(input("Enter the exponent it must be raised to: "))
    Matrix = copy.deepcopy(M)
    if n == 0:
        M = [[1,0,0],[0,1,0],[0,0,1]]
    else:
        for _ in range(n-1):
            M = MatrixMultiply(Matrix, M)
    print("Exponentiated Matrix: ")
    for row in M:
        print(row)