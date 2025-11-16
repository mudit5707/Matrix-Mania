L = list(map(int, input("Enter matrix elements separated by a space: ").split()))
R, C = map(int, input("Enter no. of rows and no. of columns separated by a space: ").split())
assert (len(L) == R*C) and R==C, "Invalid Elements of Dimensions"
M = [L[i: i+C] for i in range(0, len(L), C)]
print("Original Matrix: ")
for row in M:
    print(row)
for i in range(R):
    for j in range(i):
        M[i][j], M[j][i] = M[j][i], M[i][j]
        print(i, M)
print("The Transpose: ")
for row in M:
    print(row)
