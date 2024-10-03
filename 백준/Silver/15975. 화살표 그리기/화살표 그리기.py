import sys
a=sys.stdin.readline().rstrip()
b={}
for i in range(int(a)):
    c=list(sys.stdin.readline().rstrip().split(' '))
    b[int(c[0])]=c[1]

dic=dict(sorted(b.items()))
lis=sorted(dic.items(),key=lambda x: x[1])


dist=0

for i in range(int(a)):
    if(i==0):
        if(lis[0][1]==lis[1][1]):
            dist+=abs(int(lis[0][0])-int(lis[1][0]))
    elif(i==int(a)-1):
        if(lis[int(a)-1][1]==lis[int(a)-2][1]):
            dist+=abs(int(lis[int(a)-2][0])-int(lis[int(a)-1][0]))
    elif(i>0 and i<int(a)-1):
        if(lis[i][1]==lis[i-1][1] and lis[i][1]==lis[i+1][1]):
            dist+=min(abs(int(lis[i][0])-int(lis[i-1][0])),abs(int(lis[i][0])-int(lis[i+1][0])))
        elif(lis[i][1]!=lis[i-1][1] and lis[i][1]==lis[i+1][1]):
            dist+=abs(int(lis[i][0])-int(lis[i+1][0]))
        elif(lis[i][1]==lis[i-1][1] and lis[i][1]!=lis[i+1][1]):
            dist+=abs(int(lis[i][0])-int(lis[i-1][0]))
    else:
        print(i)
print(dist)
