# Problem: Minimum Falling Path Sum - https://leetcode.com/problems/minimum-falling-path-sum/

class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dp = [[0 for i in range(n)] for j in range(n)]
        
        dp[-1] = matrix[-1]
        
        for i in range(n - 2, -1, -1):
            for j in range(n):
                    dp[i][j] = dp[i + 1][j]
                    if j != 0:
                        dp[i][j] = min(dp[i][j], dp[i + 1][j - 1])
                    if j != n - 1:
                        dp[i][j] = min(dp[i][j], dp[i + 1][j + 1])
                    dp[i][j] += matrix[i][j]
        return min(dp[0])