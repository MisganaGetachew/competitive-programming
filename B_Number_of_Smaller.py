
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
i = j = 0
res = []
while j < m:
    while i < n and a[i] < b[j]:
        i += 1
    res.append(i)
    j += 1
print(*res)
