import sys
from collections import deque
input = sys.stdin.readline

a = int(input())
b = list(map(int, input().rstrip().split()))
c = list(map(int, input().rstrip().split()))
ans = []

def plus(a, b):
    return a + b
def minus(a, b):
    return a - b
def multi(a, b):
    return(a * b)
def devide(a, b):
    if(a < 0):
        return -(-a // b)
    else:
        return a // b
def calculate(a, b, c):
    if(c == 0):
        return plus(a, b)
    elif(c == 1):
        return minus(a, b)
    elif(c == 2):
        return multi(a, b)
    else:
        return devide(a, b)

def backtracking(b, c, count, start):
    if(count == a - 1):
        ans.append(start)
        return
    for i in range(4):
        if(c[i] != 0):
            c[i] -= 1
            backtracking(b, c, count + 1, calculate(start, b[count + 1], i))
            c[i] += 1
backtracking(b, c, 0, b[0])
maxi = max(ans)
mini = min(ans)
print(maxi)
print(mini)
