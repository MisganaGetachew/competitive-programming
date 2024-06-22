# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/



class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        def isvalid(r, c):
            return 0 <= r < len(grid) and 0 <= c < len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cnt = 0
        visited = [[False for _ in range(len(grid[0]))] for _ in range(len(grid))]
        
        
        start = None
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                    break
            if start:
                break

        if not start:
            return 0  

        stack = [start]
        while stack:
            island = stack.pop()
            r, c = island
            if not isvalid(r, c) or visited[r][c]:
                continue 
            visited[r][c] = True
            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if not isvalid(nr, nc) or grid[nr][nc] == 0:
                    cnt += 1
                elif not visited[nr][nc] and grid[nr][nc] == 1:
                    stack.append((nr, nc))
        
        return cnt

          