L = list(map(int, input("Enter matrix elements separated by a space: ").split()))
R, C = map(int, input("Enter no. of rows and no. of columns separated by a space: ").split())
assert len(L) == R*C, "Invalid Elements of Dimensions"
M = [L[i: i+C] for i in range(0, len(L), C)]
print("Original Matrix: ")
for row in M:
    print(row)
RowSums = [sum(M[i]) for i in range(R)]
ColumnSums = [sum([M[i][j] for i in range(R)]) for j in range(C)]
print("Row Sums:", RowSums)
print("Column Sums:", ColumnSums)
MR = RowSums.index(max(RowSums))
mR = RowSums.index(min(RowSums))
MC = ColumnSums.index(max(ColumnSums))
mC = ColumnSums.index(min(ColumnSums))
print("After swapping rows",MR,"and",mR)
M[MR], M[mR] = M[mR], M[MR]
for row in M:
    print (row)
print("After swapping columns",MC,"and",mC)
for i in range(R):
    M[i][MC], M[i][mC] = M[i][mC], M[i][MC]
for row in M:
    print(row)