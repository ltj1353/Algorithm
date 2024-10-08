import sys
input = sys.stdin.readline

a = int(input())
b = []
c = []
score = 0
monotonic = []

for i in range(a):
    b.append((int(input()), i))

for i in b:
    while(c and c[-1][0] < i[0]):
##        print('pop ('+str(c[-1][0])+' '+str(c[-1][1])+')')
        score += c.pop()[1]
    if(not c):
        c.append((i[0],1))
##        monotonic.append(-1)
##        print(i,c,monotonic,count,score)
        continue
    if(c[-1][0] == i[0]):
        count=c.pop()[1]
        score += count
        if(c):
            score += 1
##        if(not c):
##            monotonic.append(-1)
##        monotonic.append(c[-1][0])
        c.append((i[0],count+1))
    else:
##        monotonic.append(c[-1][0])
        c.append((i[0],1))
        score +=1
##    print(i,c,monotonic,count,score)
print(score)

##입력값, 인덱스, 모노토닉 스택값
##2 0 0
##4 1 0
##1 2 4
##2 3 4
##2 4 4
##5 5 0
##1 6 5
##2 7 5
##4 8 5
##3 9 4
##8 10 0
##9 11 0
## score = 19

##12
##2
##4
##1
##2
##2
##5
##1
##2
##4
##3
##8
##9

##5 0 0
##3 1 5
##1 2 3
##3 3 5
##7 4 0

##5
##5
##3
##1
##3
##7

##5 0 0
##5 1 0
##2 2 5
##1 3 2
##5 4 0

