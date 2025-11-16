from tabulate import tabulate
n = int(input("Enter the side of your number spiral: "))
c = 1
top = 0
bottom = n-1
left = 0
right = n-1
M = [[0]*n for _ in range(n)]
while c <= n*n :
    for i in range(left, right+1):
        M[top][i] = c
        c+=1
    top += 1
    for i in range(top, bottom+1):
        M[i][right] = c
        c+= 1
    right -= 1
    for i in range(right, left-1, -1):
        M[bottom][i] = c
        c += 1
    bottom -= 1
    for i in range(bottom, top-1, -1):
        M[i][left] = c
        c += 1
    left += 1
print(tabulate(M))
