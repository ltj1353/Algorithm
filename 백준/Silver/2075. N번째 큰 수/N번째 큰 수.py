import sys
import heapq
input = sys.stdin.readline

a = int(input().rstrip())
b = [0] * a
c = [-1000000001] * a
d = []

for i in range(a):
    b[i] = sorted(list(map(int, input().rstrip().split(' '))))

c = b[-1]
heapq.heapify(c)

for i in range(a):
    maxi = max(c[0], b[a - 2][a - 1 - i])
    if(maxi == c[0]):
        break
    else:
        j = 0
        while(c[0] < b[a - 2 - j][a - 1 - i] and a - 2 - j >= 0):
            heapq.heappush(c, b[a - 2 - j][a - 1 - i])
            heapq.heappop(c)
            j += 1
print(c[0])

# for i in range(a):
#     d = list(map(int, input().rstrip().split(' ')))
#     for j in range(a):
#         heapq.heappush(c, d[j])
#         heapq.heappop(c)

# print(c[0])