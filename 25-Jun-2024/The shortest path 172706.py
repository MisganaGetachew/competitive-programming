# Problem: The shortest path - https://basecamp.eolymp.com/en/problems/4853

from collections import defaultdict, deque
v, e = map(int, input().split())
start, end = map(int, input().split())
graph = defaultdict(list)
visited = defaultdict(int)
for _ in range(e):
    u , v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
    visited[u] = 0
    visited[v] = 0

# print(graph)
deq = deque([(start, 0)])
prev = {start:-1}
short = -1
while deq:
    node, level = deq.popleft()
    if node == end:
        short = level
        break
    for neigh in graph[node]:
        if visited[neigh]:
            continue
        prev[neigh] = node
        visited[neigh] = 1
        deq.append((neigh, level + 1))
if visited[end]:
    ans = deque()
    curr = end
    while curr != start:
        ans.appendleft(curr)
        curr = prev[curr]  
    ans.appendleft(curr)
    
    print(short)
    print(*list(ans))
else:
    print(- 1)