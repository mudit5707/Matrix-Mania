L = list(map(int, input().split()))
size = int(input())
k = 0
M = [[0]*size for _ in range(size)]
for i in range(size):
    for j in range(size):
        M[i][j] = L[k]
        k += 1
print(M)