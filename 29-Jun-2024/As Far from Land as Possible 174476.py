# Problem: As Far from Land as Possible - https://leetcode.com/problems/as-far-from-land-as-possible/description/

from collections import deque
from math import inf
from typing import List

class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        def outbound(x, y, grid):
            return x < 0 or x >= len(grid) or y < 0 or y >= len(grid[0])

        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        q = deque()
        visited = set()
        
        # Add all land cells to the queue
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    q.append((i, j, 0))
                    visited.add((i, j))
        
        if not q or len(q) == len(grid) * len(grid[0]):
            return -1
        
        max_distance = -inf
        
        while q:
            x, y, step = q.popleft()
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if not outbound(nx, ny, grid) and (nx, ny) not in visited:
                    visited.add((nx, ny))
                    if grid[nx][ny] == 0:
                        # grid[nx][ny] =  1
                        max_distance = max(max_distance, step + 1)
                        q.append((nx, ny, step + 1))
        
        return max_distance
