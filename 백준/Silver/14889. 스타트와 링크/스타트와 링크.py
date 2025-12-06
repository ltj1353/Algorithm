import sys
input = sys.stdin.readline

a = int(input())
b = [list(map(int, input().split())) for _ in range(a)]
visit = [0] * a
ans = []

def calc(team):
    s = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)):
            x, y = team[i], team[j]
            s += b[x][y] + b[y][x]
    return s

def backtracking(start, count):
    if count == a // 2:
        t1, t2 = [], []
        for i in range(a):
            if visit[i]:
                t1.append(i)
            else:
                t2.append(i)

        s1 = calc(t1)
        s2 = calc(t2)
        ans.append(abs(s1 - s2))
        return

    for i in range(start, a):
        if not visit[i]:
            visit[i] = 1
            backtracking(i + 1, count + 1)
            visit[i] = 0

backtracking(0, 0)
print(min(ans))
