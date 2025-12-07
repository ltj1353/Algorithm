import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
c = list(map(int, input().rstrip().split()))
ans = 0

def backtracking(start, visited = []):
    global ans
    if(start == b):
        if(visited):
            ans += 1
    elif(len(visited) == a):
        return
    for i in range(a):
        if(i not in visited and (not visited or visited[-1] < i)):
            visited.append(i)
            backtracking(start + c[i], visited)
            visited.pop()

backtracking(0, [])
print(ans)

