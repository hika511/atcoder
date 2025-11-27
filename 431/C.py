Yes = "Yes"
No = "No"
n, m, k = map(int, input().split())
H = list(map(int, input().split()))
B = list(map(int, input().split()))
H.sort()
B.sort()
i = 0
j = 0
ans = 0
while(i < n and j < m):
  if H[i] <= B[j]:
    i += 1
    j += 1
    ans += 1
  else:
    j += 1
if ans >= k:
  print(Yes)
else:
  print(No)