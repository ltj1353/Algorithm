a = input()
b = input()
while (b != a):
    if (len(b) == 0):
        print("0")
        exit()
    if (b[-1] == 'A'):
        b = b[:-1]
    elif (b[-1] == 'B'):
        b = b[::-1]
        b = b[1:]
    else:
        print("0")
        exit()
print("1")



##import sys
##from collections import deque
##input = sys.stdin.readline
##
##a = deque(input().rstrip())
##b = input().rstrip()
##
##isa = [0] * len(b)
##isreversed = False
##isleft = False
##isanswer = False
##depth = 0
##
##def convert(a):
##    return ''.join(a)
##
##while(len(a) < len(b)):
##    if(depth == -1):
##        break
##    elif(isa[depth] == 2):
##        depth -= 1
##        if(isleft == False):
##            a.pop()
##        else:
##            a.popleft()
##        continue
##    elif(isreversed == False):
##        if(isa[depth] == 0):
##            a.append("A")
##            isa[depth] = 1
##        else:
##            a.appendleft("B")
##            isreversed = True
##            isleft = True
##            isa[depth] = 2
##    else:
##        if(isa[depth] == 0):
##            a.appendleft("A")
##            isa[depth] = 1
##            isleft = True
##        else:
##            a.append("B")
##            isreversed = False
##            isa[depth] = 2
##    # 정답일때
##    if((convert(a) == b and isreversed == False) or ((convert(a)[::-1]) == b and isreversed == True)):
##        isanswer = True
##        # print(a,isreversed)
##        break
##    # 정답은 아니지만 부분문자열일때
##    elif(convert(a) in b or (convert(a)[::-1]) in b):
##        pass
##        # print(convert(a),b,(convert(a) in b),depth)
##    # 부분문자열이 아닐때
##    elif((convert(a) not in b) or ((convert(a)[::-1]) not in b)):
##        if(isleft == False):
##            a.pop()
##        else:
##            a.popleft()
##        depth -= 1
##
##    #     print('depth minus')
##    # print(depth)
##    # print('depth plus')
##    depth += 1
##
##if(isanswer == True):
##    print(1)
##else:
##    print(0)
