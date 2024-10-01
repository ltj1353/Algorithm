import sys

input = sys.stdin.readline
a = int(input().rstrip())
b  = list(map(int, sys.stdin.readline().rstrip().split()))
c = int(input().rstrip())
d  = list(map(int, sys.stdin.readline().rstrip().split()))
dic = {}
for i in range(a):
    dic[b[i]]=0
for i in range(c):
    if d[i] not in dic:
        sys.stdout.write('0')
    else:
        sys.stdout.write('1')
    sys.stdout.write(' ')
