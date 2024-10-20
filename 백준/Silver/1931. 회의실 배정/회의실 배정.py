import sys
input = sys.stdin.readline

a = int(input())
b = []
c = []

for i in range(a):
    b.append(list(map(int,input().split())))

b = sorted(b)
count = 0

for i in range(1,a):
    # print(b[count][1],b[i][0],b[i][1])
    if(b[count][1] <= b[i][0]):
        c.append(b[count])
        count = i
    elif(b[count][1] > b[i][1]):
        count = i
    # print(count,c)
c.append(b[count])
# print(c)
print(len(c))

