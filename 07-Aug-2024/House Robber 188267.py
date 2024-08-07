# Problem: House Robber - https://leetcode.com/problems/house-robber/

class Solution:
    def rob(self, nums: List[int]) -> int:
        maxhouse = {}
        ans = 0
        def dp(index):
            if index < 0:
                return 0
            if index == 0:
               return nums[0] 
            elif  index == 1:
                maxhouse[index]=max(nums[0],nums[1])
                return maxhouse[index]
            if index not in maxhouse:
                maxhouse[index] =max( nums[index] + dp(index - 2), dp(index - 1))
            return maxhouse[index]

        
        return dp(len(nums) - 1)