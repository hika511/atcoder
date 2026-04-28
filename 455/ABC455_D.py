# D - Card Pile Query
# https://atcoder.jp/contests/abc455/tasks/abc455_d

# カードの上下だけ記録する
N, Q = map(int, input().split())
U = [-1] * N + [i for i in range(N)]
D = [i+N for i in range(N)]
for qu in range(Q):
    c, p = map(int, input().split())
    c -= 1
    p -= 1
    # カードcより上側のカードをpの上に移動する
    U[D[c]] = -1
    U[p] = c
    D[c] = p

ans = []
for i in range(N):
    cnt = 0
    up_card = U[N+i]
    while up_card != -1:
        cnt += 1
        up_card = U[up_card]
    ans.append(cnt)

print(*ans)