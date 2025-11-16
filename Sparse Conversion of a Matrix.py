def P1():
    print("Solving P1")
    L, B = map(int, input().split())
    Matrix = []
    for i in range(L):
        Row = list(map(int, input().split()))
        assert len(Row)==B, "Invalid Number of Elements in the Row"
        Matrix.append(Row)
    Sparse = []
    for i in range(L):
        for j in range(B):
            if Matrix[i][j]==0:
                continue
            T = (i, j, Matrix[i][j])
            Sparse.append(T)
    print("Sparse Representation:")
    for T in Sparse:
        print(T, end=" ")

def P2():
    print("Solving P2")
    M1 = SparseToMatrix(input().split())
    M2 = SparseToMatrix(input().split())

def SparseToMatrix(M):
    Mat = dict()
    for i in M:
        R = int(M[1])
        C = int(M[3])
        V = int(M[5])
        Mat[(R,c)] = V
    R = max([T[0] for T in Mat.keys()])
    C = max([T[1] for T in Mat.keys()])
    M = []
    for i in range(R):
        M.append([0]*C)
    for r, c in Mat:
        M[r][c] = Mat[(r,c)]
    return M

if _name__ == "__main__":
    P1()
    P2()
