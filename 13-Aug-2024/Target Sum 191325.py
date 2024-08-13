# Problem: Target Sum - https://leetcode.com/problems/target-sum/

class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {0: 1}  

        for num in nums:
            next_dp = {}
            for sum_so_far, count in dp.items():
                next_dp[sum_so_far + num] = next_dp.get(sum_so_far + num, 0) + count
                next_dp[sum_so_far - num] = next_dp.get(sum_so_far - num, 0) + count
            dp = next_dp

        return dp.get(target, 0)