#확인용입니다
import sys
input = sys.stdin.readline

def backtracking(alist = [], visited = []):
    if(len(visited) == 6):
        print(' '.join(map(str, visited)))
        return
    for i in range(1, alist[0] + 1):
        if(not visited or (visited[-1] < alist[i])):
            visited.append(alist[i])
            backtracking(alist, visited)
            visited.pop()

a = []
while(a != [0]):
    a = list(map(int, input().rstrip().split()))
    backtracking(a, [])
    print()
