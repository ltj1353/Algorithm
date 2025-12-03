#확인용입니다
import sys
import math
input = sys.stdin.readline

a = int(input())
b = list(map(int, input().rstrip().split(' ')))
c = list(map(int, input().rstrip().split(' ')))
ans = 0

for i in range(a):
    tmp = 0
    if(b[i] - c[0] > 0):
        ans += (math.ceil((b[i] - c[0]) / c[1]) + 1)
    else:
        ans += 1

print(ans)