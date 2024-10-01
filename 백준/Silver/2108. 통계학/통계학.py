import sys
import math
from collections import Counter
import operator

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    lesser_arr, equal_arr, greater_arr = [], [], []
    for num in arr:
        if num < pivot:
            lesser_arr.append(num)
        elif num > pivot:
            greater_arr.append(num)
        else:
            equal_arr.append(num)
    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)



a = int(input())
b=[]

bsum=0
for _ in range(a):
    c=int(sys.stdin.readline())
    b.append(c)
    bsum+=c

mid=b[round(a/2)]
gap=max(b)-min(b)
b.reverse()
d = dict(Counter(b))
v = list(d.values())
k = list(d.keys())



if v.count(max(v)) > 1 :
    many = sorted(filter(lambda x: d[x] == max(v), d.keys()))[1]
else :
    many = k[v.index(max(v))]

e=quick_sort(b)
print(round(bsum/a))
print(e[a//2])
print(many)
print(gap)
