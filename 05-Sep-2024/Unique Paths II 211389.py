# Problem: Unique Paths II - https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n, m = len(obstacleGrid), len(obstacleGrid[0])
        memo = {}
        def dp(i, j):
            # out of bound and obstacle
            if i >= n or j >= m or obstacleGrid[i][j] == 1:
                return 0

            if i == n - 1 and j == m - 1:
                return 1
            if (i, j) in memo:
                return memo[(i, j)]

            memo[(i, j)] = dp(i, j + 1) + dp(i + 1, j)
            return memo[(i, j)]

        return dp(0, 0)