# Problem: Subsets - https://leetcode.com/problems/subsets/

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(start, comb):
            ans.append(comb.copy()) 
            for i in range(start, len(nums)):
                comb.append(nums[i])
                backtrack(i + 1, comb)
                comb.pop()
        
        backtrack(0, [])
        return ans