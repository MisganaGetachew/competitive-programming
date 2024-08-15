# Problem: Coin Change II - https://leetcode.com/problems/coin-change-ii/

class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = {}
        
        def rec(level, amount):
            if amount == 0:
                return 1
            if level == len(coins):
                return 0 if amount > 0 else 1
            key = (level, amount)
            if key in memo:
                return memo[key]
            count = 0
            for k in range(amount//coins[level] + 1):
                count += rec(level + 1, amount - k*coins[level])
            memo[key] = count
            return count
        return rec(0, amount)