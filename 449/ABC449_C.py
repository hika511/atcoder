# C Comfortable Distance
# https://atcoder.jp/contests/abc449/tasks/abc449_c

def search(width, S):
    if width == 0:
        return 0
    E = list("qwertyuiopasdfghjklzxcvbnm")
    E.sort()
    counter = {}
    for e in E:
        counter[e] = 0
    n = 0
    ans = 0
    while n < width:
        counter[S[n]] += 1
        if counter[S[n]] > 1:
            ans += (counter[S[n]]-1)
        n += 1
    
    while n < len(S):
        counter[S[n-width]] -= 1
        counter[S[n]] += 1
        if counter[S[n]] > 1:
            ans += (counter[S[n]]-1)
        n += 1
    return ans

N, L, R = map(int, input().split())
S = input()
print(search(R+1, S) - search(L, S))
