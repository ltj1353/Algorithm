a, b = map(int, input().split())
c = list(map(int, input().split()))
score = 0
start=0
end=0
count=0
for start in range(a):
    while(end < a and count < b):
        count += c[end]
        end += 1
    if count == b:
        score += 1
    count -= c[start]
print(score)
