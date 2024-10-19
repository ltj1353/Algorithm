#확인용
import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split(' '))
c = []

for i in range(a):
    c.append(int(input().rstrip()))
c = sorted(c)

start = 1
end = c[-1] - c[0] + 1
ans = 0

while(start <= end):
    mid = (end + start) // 2
    count = 1
    d = c[0]
    for i in range(1, a):
        if((c[i] - d) >= mid):
            count += 1
            d = c[i]

    # print(start,mid,end,count,ans)
    if (count >= b):
        # print('yes')
        start = mid + 1
    else:
        # print('no')
        end = mid - 1
        ans = mid - 1
# print(start,mid,end,count,ans)
print(ans)
