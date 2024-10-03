import sys

dic={}

for _ in range(1000000):
    a = sys.stdin.readline().rstrip()
    if a=='':
        break
    if a not in dic:
        dic[a]=1
    else:
        dic[a]+=1

leng=sum(dic.values())
dicti=sorted(dic)


for i in dicti:
    if i=='':
        break
    print(i, format(dic[i]/leng*100,'.4f'))
