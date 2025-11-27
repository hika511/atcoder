X = int(input())
N = int(input())
W = list(map(int, input().split()))
Q = int(input())
isWearN = [0]*N
for i in range(Q):
  P = int(input())
  P -= 1
  if isWearN[P] == 0:
    X += W[P]
    isWearN[P] = 1
    print(X)
  elif isWearN[P] == 1:
    X -= W[P]
    isWearN[P] = 0
    print(X)
  else:
    print("ERROR")
    