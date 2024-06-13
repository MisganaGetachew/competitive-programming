# Problem: From adjacency matrix to adjacency lists - https://basecamp.eolymp.com/en/problems/3981

from collections import defaultdict
n = int(input())
graph = defaultdict(list)
for i in range(n ):
    raw = list(map(int, input().split()))
    for j in range(len(raw)):
        if raw[j] == 1:
          graph[i + 1].append(j+1)
# print(graph)
for key, val in graph.items():
    print(len(val), *val)