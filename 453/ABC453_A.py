N = int(input())
S = input()
ans = ""
for i in range(N):
    if S[i] != "o":
        ans = S[i:]
        break
print(ans)