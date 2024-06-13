# Problem: Find Center of Star Graph - https://leetcode.com/problems/find-center-of-star-graph/

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        from collections import defaultdict
        graph = defaultdict(list)
        for edge in edges:
            u, v = edge
            graph[u].append(v)
            graph[v].append(u)

        for key, val in graph.items():
            print(val)
            if len(val) == len(edges):
                return key
        