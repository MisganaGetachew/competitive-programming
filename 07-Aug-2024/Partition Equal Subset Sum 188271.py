# Problem: Partition Equal Subset Sum - https://leetcode.com/problems/partition-equal-subset-sum/

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo={}
        if sum(nums)%2:
            return False
        def solve(i,c):
            if i>=len(nums):
                return c==(sum(nums)//2)
            if(i,c)not in memo:
                memo[(i,c)]=solve(i+1,c+nums[i]) or solve(i+1,c)
            
            return memo[(i,c)]
        return solve(0,0)


      


        

            

        