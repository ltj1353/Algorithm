a, b = input().split()
a = list(map(int, reversed(list(a))))
b = list(map(int, reversed(list(b))))
if len(a)>len(b):
    big=len(a)
else:
    big=len(b)
c=[]
if len(a)<big:
    for i in range(big-len(a)):
        a.append(0)
if len(b)<big:
    for i in range(big-len(b)):
        b.append(0)

carry=0
for i in range(big):
    c.append((a[i]+b[i]+carry)%10)
    carry = (a[i]+b[i]+carry)//10
    if i == big-1 and carry > 0:
        c.append(carry)


c=list(reversed(c))
if c[0]==0:
    del c[0]
print(*c,sep='')
