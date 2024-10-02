import sys
a = int(input())
b={}
s={}
for _ in range(a):
    b = sys.stdin.readline().rstrip().split(' ')
    if b[0]=='add':
        s[int(b[1])]=0
    elif b[0]=='remove':
        if int(b[1]) in s:
            del s[int(b[1])]
    elif b[0]=='check':
        if int(b[1]) in s:
            sys.stdout.write('1')
            sys.stdout.write('\n')
        else:
            sys.stdout.write('0')
            sys.stdout.write('\n')
    elif b[0]=='toggle':
        if int(b[1]) in s:
            del s[int(b[1])]
        else:
            s[int(b[1])]=0
    elif b[0]=='all':
        s={}
        for i in range(1,21):
            s[i]=0
    elif b[0]=='empty':
        s={}
