# D Make Target 2
# https://atcoder.jp/contests/abc449/tasks/abc449_d

L, R, D, U = map(int, input().split())

ans = 0
for h in range(D, U+1):
    if h % 2 == 1:
        if L < 0:
            if abs(L) >= abs(h):
                ans += abs(L)//2 - abs(h)//2
        elif L > 0:
            if abs(L) >= abs(h):
                if max(abs(L), abs(h)) % 2 == 0:
                    ans += 1
                ans -= abs(L)//2 - abs(h)//2
        if R > 0:
            if abs(R) >= abs(h):
                ans += abs(R)//2 - abs(h)//2
        elif R < 0:
            if abs(R) >= abs(h):
                if max(abs(R), abs(h)) % 2 == 0:
                    ans += 1
                ans -= abs(R)//2 - abs(h)//2
    else:
        if L < 0:
            if abs(L) <= abs(h):
                ans += abs(L)
            else:
                ans += abs(L)//2 + abs(h)//2
        elif L > 0:
            if max(abs(L), abs(h)) % 2 == 0:
                ans += 1
            if abs(L) <= abs(h):
                ans -= abs(L)
            else:
                ans -= abs(L)//2 + abs(h)//2
        if R > 0:
            if abs(R) <= abs(h):
                ans += abs(R)
            else:
                ans += abs(R)//2 + abs(h)//2 
        elif R < 0:
            if max(abs(R), abs(h)) % 2 == 0:
                ans += 1
            if abs(R) <= abs(h):
                ans -= abs(R)
            else:
                ans -= abs(R)//2 + abs(h)//2 
        if L <= 0 and R >= 0:
            ans += 1
print(ans)