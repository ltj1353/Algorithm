import sys
input = sys.stdin.readline

a, b = map(int,input().rstrip().split())
if(a == 1 or b == 1 or (a == 2 and b == 2)):
    print(1)
elif(a == 2):
    if(b > 8):
        print(4)
    else:
        print(int((b + 1) // 2))
elif(a > 2):
    if(b < 5):
        print(b)
    elif(b == 5 or b == 6):
        print(4)
    else:
        print(b-2)
