import heapq
X = int(input())
Q = int(input())
A = []
mid = X
small = []
big = []

for _ in range(Q):
    a, b = map(int, input().split())
    if a <= mid and b >= mid:
        heapq.heappush(small, -1*a)
        heapq.heappush(big, b)
        A.append(mid)
    elif a >= mid and b <= mid:
        heapq.heappush(big, a)
        heapq.heappush(small, -1*b)
        A.append(mid)
    if a > mid and b > mid:
        heapq.heappush(big, a)
        heapq.heappush(big, b)
        heapq.heappush(small, -1*mid)
        mid = heapq.heappop(big)
        A.append(mid)
    elif a < mid and b < mid:
        heapq.heappush(small, -1*a)
        heapq.heappush(small, -1*b)
        heapq.heappush(big, mid)
        mid = heapq.heappop(small) * -1
        A.append(mid)

        
for t in A:
    print(t)