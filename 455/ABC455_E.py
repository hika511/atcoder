# E - Unbalanced ABC Substrings
# https://atcoder.jp/contests/abc455/tasks/abc455_e

'''
N(N+1)//2 - {n(A==B) + n(B==C) + n(C==A) - 2n(A==B==C)}
= N(N+1)//2 - n(A==B) - n(B==C) - n(C==A) + 2n(A==B==C)
'''

from collections import Counter

N = int(input())
S = input()
# A[i]: i文字目までのまでのAの個数
A = [0] * (N+1)
B = [0] * (N+1)
C = [0] * (N+1)

for i in range(len(S)):
    if S[i] == "A":
        A[i+1] = A[i] + 1
        B[i+1] = B[i]
        C[i+1] = C[i]
    elif S[i] == "B":
        A[i+1] = A[i]
        B[i+1] = B[i] + 1
        C[i+1] = C[i]
    else:
        A[i+1] = A[i]
        B[i+1] = B[i]
        C[i+1] = C[i] + 1
A_B = [a-b for a, b in zip(A, B)]
A_C = [a-c for a, c in zip(A, C)]
B_C = [b-c for b, c in zip(B, C)]
counter_ABC = Counter(zip(A_B, A_C))

ans_ABC = 0
for k, v in counter_ABC.items():
    ans_ABC += v * (v-1) // 2

ans_AB = 0
counter_AB = Counter(A_B)
for k, v in counter_AB.items():
    ans_AB += v * (v-1) // 2

ans_AC = 0
counter_AC = Counter(A_C)
for k, v in counter_AC.items():
    ans_AC += v * (v-1) // 2

ans_BC = 0
counter_BC = Counter(B_C)
for k, v in counter_BC.items():
    ans_BC += v * (v-1) // 2

ans = N * (N+1) // 2 - ans_AB - ans_AC - ans_BC + 2 * ans_ABC
print(ans)