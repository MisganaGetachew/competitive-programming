# Problem: Operations on graphs - https://basecamp.eolymp.com/en/problems/2472

from collections import defaultdict
n = int(input())
opp = int(input())
graph = defaultdict(list)
vertex = []
# matrix = []
# val = None
for i in range(1, opp + 1):
    raw = list(map(int, input().split())) 
    if raw[0] == 1:
        u, v = raw[1:]
        graph[u].append(v)
        graph[v].append(u)
    else:
        print(*graph[raw[1]])
