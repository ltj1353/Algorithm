import sys
input = sys.stdin.readline

a = int(input().rstrip())
b = sorted(list(map(int,input().rstrip().split())))
c = 1

if(a == 1):
    print(b[0] * b[0])
elif(a == 2):
    print(b[0] * b[1])
elif(a % 2 == 1):
    print(b[a // 2] * b[a // 2])
else:
    print(b[(a + 1) // 2] * b[(a + 1) // 2 - 1])