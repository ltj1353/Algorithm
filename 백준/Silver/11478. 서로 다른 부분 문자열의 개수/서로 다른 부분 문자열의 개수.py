import sys
a=list(sys.stdin.readline().rstrip())
dic={}

for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        dic["".join(a[i:j])]=0
print(len(dic))
