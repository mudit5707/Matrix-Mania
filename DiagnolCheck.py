L = list(map(int, input("Enter matrix elements separated by a space: ").split()))
R, C = map(int, input("Enter no. of rows and no. of columns separated by a space: ").split())
assert len(L) == R*C, "Invalid"
c = 0
M = []
for i in range(R):
    row = []
    for j in range(C):
        row.append(L[c])
        c+=1
    M.append(row)
print("Original Matrix: ")
for row in M:
    print(row)
Diagonal = True
for i in range(min([R,C]) - 1):
    if M[i][i] != M[i+1][i+1]:
        Diagonal = False
        break
if Diagonal:
    print("Yes")
else:
    print("False")