# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        u = deque()
        row, col = len(grid), len(grid[0])
        visited = set()
        minute = 0
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    u.append((r,c))
                    visited.add((r,c))
        dir = [(-1,0), (1,0), (0,-1), (0,1)]
        while u:
            bef = len(visited)
            for i in range(len(u)):
                r, c = u.popleft()
                for dx, dy in dir:
                    new_r = r + dx
                    new_c = c + dy
                    if new_r < 0 or new_c < 0 or new_r > len(grid)-1 or new_c > len(grid[0])-1 or grid[new_r][new_c] == 0:
                        continue
                    if (new_r, new_c) not in visited:
                        visited.add((new_r,new_c))
                        grid[new_r][new_c] = 2
                        u.append((new_r,new_c))
            if len(visited) == bef:
                break
            minute += 1
        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    return -1
        return minute
        


        
       
        
