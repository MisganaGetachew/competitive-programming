# Problem: D - Playlist - https://codeforces.com/gym/536373/problem/D

import heapq
n, k = map(int, input().split())
s = []
for _ in range(n):
    l, b = map(int, input().split())
    s.append([l, b])
s.sort(key=lambda x: -x[1])
heap = []
ttl = 0
mx = 0
for l, b in s:
    heapq.heappush(heap, l)
    ttl += l
    if len(heap) > k:
        ttl -= heapq.heappop(heap)
    temp = ttl * b
    mx = max(mx, temp)
print(mx)
