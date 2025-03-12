#확인용
import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
c = int(input().rstrip())

hour = c // 60
minute = c % 60

a += hour
b += minute

if(b >= 60):
    b -= 60
    a += 1
if(a >= 24):
    a -= 24
print(a, b)