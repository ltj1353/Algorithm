#확인용입니다
import sys
input = sys.stdin.readline

a = list(map(int, input().rstrip()))
b = list(map(int, input().rstrip()))
c = list(map(int, input().rstrip()))
d = list(map(int, input().rstrip()))
e = int(input())
f = [[] for _ in range(e)]
A, B, C, D = 2, 2, 2, 2

for i in range(e):
    f[i] = list(map(int, input().rstrip().split()))

for i in range(e):
    if(f[i][0] == 1):
        if(a[A] != b[B - 4]):
            if(b[B] != c[C - 4]):
                if(c[C] != d[D - 4]):
                    D += f[i][1]
                C -= f[i][1]
            B += f[i][1]
        A -= f[i][1]
    elif(f[i][0] == 2):
        if(b[B] != c[C - 4]):
            if(c[C] != d[D - 4]):
                D -= f[i][1]
            C += f[i][1]
        if(a[A] != b[B - 4]):
            A += f[i][1]
        B -= f[i][1]
    elif(f[i][0] == 3):
        if(b[B] != c[C - 4]):
            if(a[A] != b[B - 4]):
                A -= f[i][1]
            B += f[i][1]
        if(c[C] != d[D - 4]):
            D += f[i][1]
        C -= f[i][1]
    else:
        if(c[C] != d[D - 4]):
            if(b[B] != c[C - 4]):
                if(a[A] != b[B - 4]):
                    A += f[i][1]
                B -= f[i][1]
            C += f[i][1]
        D -= f[i][1]
    A %= 8
    B %= 8
    C %= 8
    D %= 8
print(a[(A - 2) % 8] + 2 * b[(B - 2) % 8] + 4 * c[(C - 2) % 8] + 8 * d[(D - 2) % 8])
