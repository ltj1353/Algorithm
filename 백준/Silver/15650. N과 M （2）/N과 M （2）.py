import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())

def backtracking(visited = []):
    if(len(visited) == b):
        print(' '.join(map(str, visited)))
        return

    for i in range(1, a + 1):
        if(not visited or (i not in visited and visited[-1] < i)):
            visited.append(i)
            backtracking(visited)
            visited.pop()
backtracking([])
