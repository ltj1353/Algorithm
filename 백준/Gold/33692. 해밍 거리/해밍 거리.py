import sys
input = sys.stdin.readline

a, b = map(int, input().rstrip().split())
c = len(bin(b)) - 2
low = ''
high = ''

a = bin(a).lstrip('0b').zfill(c)
b = bin(b).lstrip('0b').zfill(c)

i = 0
while(a[i] == b[i]):
    low += a[i]
    high += b[i]
    i += 1
low += '0'
high += '1'
for i in range(len(low), c):
    low += '1'
    high += '0'
# print(a, b)
# print(low, high)
print(int(low, 2), int(high, 2))
