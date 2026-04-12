N = int(input())
L = list(map(int, input().split()))

ans = 0
for bit in range(1<<N):
    X = 0.5
    p = 0
    for i in range(N):
        if bit & (1<<i):
            if X < 0 and X + L[i] > 0:
                p += 1
            X += L[i]
        else:
            if X > 0 and X - L[i] < 0:
                p += 1
            X -= L[i]
    ans = max(ans, p)
print(ans)