# Problem: B - Network Topology - https://codeforces.com/gym/531416/problem/B

from collections import defaultdict


n, m = map(int, input().split())
graph = defaultdict(list)

for _ in range(m):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)


def bus(graph, n, m):
    count = [0] * (n + 1)
    for i in range(1, n + 1):
        count[i] = len(graph[i])

    ones = count.count(1)
    twos = count.count(2)

    return ones == 2 and twos == (n - 2)


def ring(graph, n, m):
    if m != n:
        return False

    for i in range(1, n + 1):
        if len(graph[i]) != 2:
            return False

    return True


def star(graph, n, m):
    count = [0] * (n + 1)
    for i in range(1, n + 1):
        count[i] = len(graph[i])

    center = count.count(n - 1)
    leaf = count.count(1)

    return center == 1 and leaf == (n - 1)


if bus(graph, n, m):
    print("bus topology")
elif ring(graph, n, m):
    print("ring topology")
elif star(graph, n, m):
    print("star topology")
else:
    print("unknown topology")
