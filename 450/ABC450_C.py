# C Puddles
# https://atcoder.jp/contests/abc450/tasks/abc450_c
from collections import deque
h, w = map(int, input().split())
S = []
for i in range(h):
    S.append(list(input()))

def edgeloc(h, w):
    edges = []
    for hi in range(h):
        for wi in range(w):
            if hi == 0 or hi == h-1 or wi == 0 or wi == w-1:
                edges.append((hi, wi))
    return edges

def adjloc(x, y, h, w):
    adjs = []
    if x-1 >= 0:
        adjs.append((x-1, y))
    if y-1 >= 0:
        adjs.append((x, y-1))
    if x+1 < h:
        adjs.append((x+1, y))
    if y+1 < w:
        adjs.append((x, y+1))
    return adjs

for hi, wi in edgeloc(h, w):
    if S[hi][wi] == ".":
        q = deque()
        S[hi][wi] = "#"
        for hadj, wadj in adjloc(hi, wi, h, w):
            q.append((hadj, wadj))
        while q:
            hj, wj = q.popleft()
            if S[hj][wj] == ".":
                S[hj][wj] = "#"
                for hadj, wadj in adjloc(hj, wj, h, w):
                    q.append((hadj, wadj))

ans = 0
for hi in range(h):
    for wi in range(w):
        if S[hi][wi] == ".":
            q = deque()
            S[hi][wi] = "#"
            for hadj, wadj in adjloc(hi, wi, h, w):
                q.append((hadj, wadj))
            while q:
                hj, wj = q.popleft()
                if S[hj][wj] == ".":
                    S[hj][wj] = "#"
                    for hadj, wadj in adjloc(hj, wj, h, w):
                        q.append((hadj, wadj))
            ans += 1
print(ans)