import sys
a = int(input())
c=[0]*10001  
for _ in range(a):
    b=int(sys.stdin.readline())
    c[b]+=1

for i in range(10001):
    if (c[i] > 0):
        for j in range(c[i]):
            sys.stdout.write(str(i)+'\n')
