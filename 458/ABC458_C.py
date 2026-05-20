S = input()

l = len(S)
ans = 0
for i in range(l):
    if S[i] == "C":
        ans += min(i+1, l-i)
        
print(ans)