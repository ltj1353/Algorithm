import sys
input = sys.stdin.readline

a = int(input().rstrip())
b = {"ChongChong" : 1}

for i in range(a):
    c, d = input().rstrip().split(' ')
    if(c in b):
        b[d] = 1
    elif(d in b):
        b[c] = 1
print(len(b.keys()))