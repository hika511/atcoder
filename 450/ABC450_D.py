# Minimize Range
# https://atcoder.jp/contests/abc450/tasks/abc450_d

n, k = map(int, input().split())
A = list(map(int, input().split()))

for i in range(len(A)):
    A[i] %= k

A = sorted(set(A))
ans = A[-1] - A[0]
for i in range(len(A)-1):
    A[i] += k
    ans = min(ans, A[i] - A[i+1])
print(ans)