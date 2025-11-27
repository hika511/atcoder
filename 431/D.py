# 全てのパーツを体に
N = int(input())
W = [0]
H = [0]
B = [0]

# 全てのパーツの重さの合計
S = 0

for i in range(N):
    w, h, b = map(int, input().split())
    W.append(w)
    H.append(h)
    B.append(b)
    S += w
    
# dp[i][j] i番目までの商品がある時、重さj以下で達成できる最大の評価値
# 重さの上限: S // 2

S = S//2
dp = []
tmp = [0] * (S+1)

for i in range(N+1):
    dp.append(tmp[:])

if N == 1:
    print(B[1])
    exit(0)

for i in range(1, N+1):
    for j in range(0, S+1):
        if (j-W[i]) < 0:
            dp[i][j] = dp[i-1][j] + B[i]
        else:
            dp[i][j] = max(dp[i-1][j-W[i]]+H[i], dp[i-1][j]+B[i])

print(dp[N][S])