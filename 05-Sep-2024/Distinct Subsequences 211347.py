# Problem: Distinct Subsequences - https://leetcode.com/problems/distinct-subsequences/description/

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n, m = len(s), len(t)
        memo = {}

        def dp(i, j):
            if j == m:
                return 1
            
            if i == n:
                return 0

            if (i, j) in memo:
                return memo[(i, j)]
            
            if s[i] == t[j]:
                memo[(i, j)] = dp(i + 1, j + 1) + dp(i + 1, j)
            else:
                memo[(i, j)] = dp(i + 1, j)
            return memo[(i, j)]
        
        return dp(0, 0)