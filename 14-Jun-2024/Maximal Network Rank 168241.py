# Problem: Maximal Network Rank - https://leetcode.com/problems/maximal-network-rank/description/

from collections import defaultdict
class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(int)
        connected = set()

        for road in roads:
            u, v = road
            graph[u] += 1
            graph[v] += 1
            connected.add((u, v))
            # connected.add((v, u))


        # print(graph)
        # print(connected)
        mx = 0 
        for i in range(n):
            for j in range(i + 1, n):
                current = graph[i] + graph[j] 
                if (i, j) in connected or (j, i) in connected:
                 current -= 1
                mx = max(mx, current)

        return mx