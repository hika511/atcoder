T = int(input())
ans_dict = []
for case in range(T):
    N, H = map(int, input().split())
    TLU = []
    TLU.append([0, H, H])
    for i in range(N):
        TLU.append(list(map(int, input().split())))
    TLU = sorted(TLU, key=lambda x: x[0])
    can_reach = [[H, H]]
    ans = True
    for i in range(1, N+1):
        t, l, u = TLU[i]
        t -= TLU[i-1][0]
        can_reach.append([can_reach[i-1][0]-t, can_reach[i-1][1]+t])
        if l > can_reach[i][0]:
            can_reach[i][0] = l
        if u < can_reach[i][1]:
            can_reach[i][1] = u
        if can_reach[i][1] - can_reach[i][0] < 0:
            ans = False
            break
    if ans:
        ans_dict.append("Yes")
    else:
        ans_dict.append("No")
for a in ans_dict:
    print(a)