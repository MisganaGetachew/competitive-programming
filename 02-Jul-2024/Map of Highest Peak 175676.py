# Problem: Map of Highest Peak - https://leetcode.com/problems/map-of-highest-peak/description/

class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        m, n = len(isWater), len(isWater[0])
        height = [[-1] * n for _ in range(m)]
        q = deque()
        visited = set()

        for row in range(len(isWater)):
            for col in range(len(isWater[0])):
                if isWater[row][col] == 1:
                    q.append((row, col, 0))
                    height[row][col] = 0
        dir = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        while q:
            r, c, step = q.popleft()

            for dx, dy in dir:
                X = dx + r
                Y = dy + c
                if 0 <= X < m and 0 <= Y < n and height[X][Y] == -1:
                # height[X][Y] = height[r][c] + 1
                # q.append((X, Y))
                    height[X][Y] = step  + 1
                    q.append((X,Y, step + 1))
        return height


                
                
            