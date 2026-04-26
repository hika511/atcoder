N, K = map(int, input().split())
A = list(map(int, input().split()))
counter = {}
A.sort()
prev = -1
for a in A:
    if a == prev:
        counter[a] += 1
    else:
        counter[a] = 1
    prev = a
sums = []
for k, v in counter.items():
    sums.append(k * v)
sums = sorted(sums, reverse=True)
ans = 0
for i in range(len(sums)):
    if i < K:
        continue
    else:
        ans += sums[i]
print(ans)