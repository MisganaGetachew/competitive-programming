# Problem: Detonate the Maximum Bombs - https://leetcode.com/problems/detonate-the-maximum-bombs/description/

from collections import defaultdict
import math
from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        n = len(bombs)
        adj = defaultdict(list)

        def distance(x1, y1, x2, y2):
            return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

        for i in range(n):
            for j in range(n):
                if i != j:
                    x1, y1, r1 = bombs[i]
                    x2, y2, _ = bombs[j]
                    if distance(x1, y1, x2, y2) <= r1:
                        adj[i].append(j)
 
        def dfs(start):
            stack = [start]
            visited = set()
            while stack:
                node = stack.pop()
                if node not in visited:
                    visited.add(node)
                    for neighbor in adj[node]:
                        if neighbor not in visited:
                            stack.append(neighbor)
            return len(visited)
    
        max_detonations = 0
        for i in range(n):
            max_detonations = max(max_detonations, dfs(i))
        
        return max_detonations
