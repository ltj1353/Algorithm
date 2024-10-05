import sys

n = int(sys.stdin.readline().rstrip())
A = []
for i in range(n):
    A.append((int(sys.stdin.readline().rstrip()), i))
A = sorted(A)
maxi = 0
for i in range(n):
    maxi = max(maxi, A[i][1]-i)

print(maxi+1)