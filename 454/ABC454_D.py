# D - (xx)
# https://atcoder.jp/contests/abc454/tasks/abc454_d

from collections import deque
def remove_xx(S):
    len_S = len(S)
    if len_S < 4:
        return S
    q = deque()
    q.append(S[0])
    q.append(S[1])
    q.append(S[2])
    len_q = 3
    for i in range(3, len_S):
        q.append(S[i])
        len_q += 1
        if len_q < 4:
            continue
        s1 = q.pop() 
        s2 = q.pop()
        s3 = q.pop()
        s4 = q.pop()
        len_q -= 4
        if s1 == ")" and s2 == "x" and s3 == "x" and s4 == "(":
            q.append("x")
            q.append("x")
            len_q += 2
        else:
            q.append(s4)
            q.append(s3)
            q.append(s2)
            q.append(s1)
            len_q += 4
    return "".join(q)

T = int(input())
for _ in range(T):
    A = input()
    B = input()
    A = remove_xx(A)
    B = remove_xx(B)
    if A == B:
        print("Yes")
    else:
        print("No")