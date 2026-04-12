T, X = map(int, input().split())
A = list(map(int, input().split()))
print(0, A[0])
prev = A[0]
for i in range(1, T+1):
    if abs(prev - A[i]) >= X:
        print(i, A[i])
        prev = A[i]
        