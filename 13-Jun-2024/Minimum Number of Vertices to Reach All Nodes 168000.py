# Problem: Minimum Number of Vertices to Reach All Nodes - https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/

from collections import defaultdict
class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        # {1: [0], 2: [0, 4], 5: [2], 4: [3]}
        # for i in range(n):
        for edge in edges:

            u , v = edge
            graph[v].append(u)
        ans = []
        for i in range(n):
            if not graph[i]:
                ans.append(i)
        return ans

