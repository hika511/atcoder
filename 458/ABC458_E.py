MOD = 998244353
MAX = 2 * 10 ** 6 + 7
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

def cmb(n, r):
    if r < 0 or n < r:
        return 0
    r = min(r, n-r)
    return fact[n] * factinv[r] * factinv[n-r] % MOD
 
for i in range(2, MAX+1):
    fact.append((fact[-1]*i) % MOD)
    inv.append((-inv[MOD%i] * (MOD//i)) % MOD)
    factinv.append((factinv[-1] * inv[-1]) % MOD)

ans = 0
x1, x2, x3 = map(int, input().split())
for k in range(1, min(x2+1, x1)+1):
    ans = (ans + cmb(x2+1, k) * cmb(x1-1, x1-k) * cmb(x2+x3-k, x3)) % MOD
    
print(ans)