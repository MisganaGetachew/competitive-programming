# Problem: Cities and road - https://basecamp.eolymp.com/en/problems/992

from collections import Counter
n = int(input())
# print ("%d %d\n" % (n/10, n%10))
count = 0
for _ in range(n):
    graph = list(map(int, input().split()))
    c = Counter(graph)
    count += c[1]

print(count//2)