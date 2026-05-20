H, W = map(int, input().split())
table = [[0]*W for _ in range(H)]

for x1 in range(W):
    for y1 in range(H):
        for x2 in range(W):
            for y2 in range(H):
                if abs(x1-x2)+abs(y1-y2) == 1:
                    table[y1][x1] += 1
for t in table:
    print(*t)