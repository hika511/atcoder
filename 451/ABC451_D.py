# Concat Power of 2
# https://atcoder.jp/contests/abc451/tasks/abc451_d

N = int(input())
MAX_GOODNUM = int(1e9)
MAX_DIGIT = len(str(MAX_GOODNUM))

# print(MAX_GOODNUM)
# print(MAX_DIGIT)


# n桁の2の冪数のリストをpower_list[n]に格納
power_list = [[] for _ in range(MAX_DIGIT)]
good_list = [[] for _ in range(MAX_DIGIT)]

pp = 1
while pp <= MAX_GOODNUM:
    power_list[len(str(pp))].append(pp)
    pp *= 2
    
# print(list_good)

good_list[1] = power_list[1]
for i in range(2, MAX_DIGIT):
    for j in range(i, 0, -1):
        for p in power_list[j]:
            if i == j:
                good_list[i].append(p)
            else:
                for g in good_list[i-j]:
                    good_list[i].append(int(str(g)+str(p)))

ans = []
for i in range(1, MAX_DIGIT):
    ans.extend(good_list[i])

ans = sorted(set(ans))
print(ans[N-1])
            