# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def dip(n):
            if n < 3:
                return n
            else:
                if n in memo:
                    return memo[n]
                memo[n] = dip(n - 2)  + dip(n - 1)
                return memo[n]
        return dip(n)