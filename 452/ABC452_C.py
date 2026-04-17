# ABC452 C Fishbones
# https://atcoder.jp/contests/abc452/tasks/abc452_c

N = int(input())
MAX = 11

# 文字数ごとに、n文字目に入りうる文字を管理
# check[文字数][n文字目のidx] = その文字数のn文字目に入りうる文字の集合
check = [[set() for _ in range(MAX)] for _ in range(MAX)]

A = []
B = []
for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b-1)

M = int(input())
S = []
for i in range(M):
    s = input()
    S.append(s)
    for j in range(len(s)):
        check[len(s)][j].add(s[j])

for i in range(M):
    # S[i]: 肋骨に書く文字
    ans_exist = True
    if len(S[i]) != N:
        print("No")
        continue
    for j in range(len(S[i])):
        if S[i][j] in check[A[j]][B[j]]:
            continue
        else:
            ans_exist = False
            break
    if ans_exist:
        print("Yes")
    else:
        print("No")
