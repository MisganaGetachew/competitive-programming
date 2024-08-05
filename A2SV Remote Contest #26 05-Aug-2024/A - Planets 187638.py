# Problem: A - Planets - https://codeforces.com/gym/540348/problem/A

from collections import defaultdict

t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    orbit = list(map(int, input().split()))
    graph = defaultdict(int)

    for i in range(n):
        graph[orbit[i]] += 1

    ans = 0

    for key in graph:
        if graph[key] > c:
            # print(graph[key])
            ans += c
        else:
            ans += graph[key]
    print(ans)
