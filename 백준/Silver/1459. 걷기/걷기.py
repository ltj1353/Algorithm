import sys
input = sys.stdin.readline

a, b, c, d = map(int, input().rstrip().split())
e = abs(a - b)
if(e % 2):
    print((min((c * 2), d) * (min(a, b)) + min(c, d) * (e - 1) + c))
else:
    print((min((c * 2), d) * (min(a, b)) + min(c, d) * e))
