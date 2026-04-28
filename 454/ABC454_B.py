# B - Mapping
# https://atcoder.jp/contests/abc454/tasks/abc454_b

N, M = map(int, input().split())
F = list([x-1 for x in map(int, input().split())])

who_wear = {i:[] for i in range(M)}
for i in range(N):
    who_wear[F[i]].append(i)
    
q1 = True
q2 = True
for i in range(M):
    if len(who_wear[i]) >= 2:
        q1 = False
        break
print("Yes" if q1 else "No")

for i in range(M):
    if len(who_wear[i]) <= 0:
        q2 = False
        break
print("Yes" if q2 else "No")
