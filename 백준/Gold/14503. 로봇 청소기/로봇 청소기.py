import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
c, d, e = map(int, input().rstrip().split())
f = [[] for _ in range(a)]
count = 0
for i in range(a):
    f[i] = list(map(int, input().rstrip().split()))

def move(c, d, e, f, check, count):
    while(check):
        if(f[c][d] == 0):
            f[c][d] = 2
            count += 1
        if(f[c - 1][d] != 0 and f[c + 1][d] != 0 and f[c][d - 1] != 0 and f[c][d + 1] != 0):
            if(e == 0):
                c += 1
            elif(e == 1):
                d -= 1
            elif(e == 2):
                c -= 1
            else:
                d += 1
            if(f[c][d] == 1):
                check = 0
                return count
        else:
            e -= 1
            if(e == -1):
                e = 3
                d -= 1
                if(f[c][d] != 0):
                    d += 1
            elif(e == 0):
                c -= 1
                if(f[c][d] != 0):
                    c += 1
            elif(e == 1):
                d += 1
                if(f[c][d] != 0):
                    d -= 1
            else:
                c += 1
                if(f[c][d] != 0):
                    c -= 1
count = move(c, d, e, f, 1, 0)
print(count)