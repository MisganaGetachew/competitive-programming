# Problem: Number of Islands - https://leetcode.com/problems/number-of-islands/

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        direction = [[0, 1], [0,-1],  [1, 0], [-1, 0]]
        if not grid:
            return 0 
        rows, cols = len(grid), len(grid[0])
        island = 0
        visited = set()

        def dfs(r, c):
            stack = [(r, c)]
            visited.add((r, c))
            while stack:
                row, col = stack.pop()
                for x, y in direction:
                    X = x + row
                    Y = y + col
                    if (X in range(rows) and 
                    Y in range(cols) and 
                    grid[X][Y] == "1" and
                    (X, Y) not in visited):
                        stack.append((X,Y))
                        visited.add((X,Y))
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visited:
                    dfs(r,c)
                    island += 1
        return island
                

