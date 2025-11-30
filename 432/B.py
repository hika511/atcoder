N, M = map(int, input().split())
w_cnt = [0] * (M+1)
w_sum = [0] * (M+1)

for i in range(1, N+1):
    A, B = map(int, input().split())
    w_cnt[A] += 1
    w_sum[A] += B
    
for i in range(1, M+1):
    w_sum[i] = w_sum[i]/w_cnt[i]
    print(w_sum[i])