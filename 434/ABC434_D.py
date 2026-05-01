N = int(input())
SIZE = 2000
A = [[0] * (SIZE+2) for _ in range(SIZE+2)]
B = [[0] * (SIZE+2) for _ in range(SIZE+2)]
for i in range(1, N+1):
    u, d, l, r = map(int, input().split())
    # 二次元imos法
    A[u][l] += 1
    A[u][r+1] -= 1
    A[d+1][l] -= 1
    A[d+1][r+1] += 1
    # 雲iについてiを加算
    B[u][l] += i
    B[u][r+1] -= i
    B[d+1][l] -= i
    B[d+1][r+1] += i

cloud_uncovered = 0
one_cloud_covered = [0 for _ in range(N+1)]
for i in range(1, SIZE+1):
    for j in range(1, SIZE):
        A[i][j+1] += A[i][j]
        B[i][j+1] += B[i][j]

for j in range(1, SIZE+1):
    for i in range(1, SIZE):
        A[i+1][j] += A[i][j]
        B[i+1][j] += B[i][j]

for i in range(1, SIZE+1):
    for j in range(1, SIZE+1):
        if A[i][j] == 0:
            cloud_uncovered += 1
        if A[i][j] == 1:
            one_cloud_covered[B[i][j]] += 1
        
for i in range(1, N+1):
    print(cloud_uncovered + one_cloud_covered[i])
        