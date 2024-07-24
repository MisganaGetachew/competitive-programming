# Problem: Minimum Replacements to Sort the Array - https://leetcode.com/problems/minimum-replacements-to-sort-the-array/

class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        op = 0
        for i in range(len(nums)-2, -1, -1 ):
            if nums[i] > nums[i + 1]:
                n = ceil(nums[i]/nums[i + 1])
                x = ceil((n * nums[i + 1] - nums[i]) /n)
                op += n - 1 
                nums[i]  = nums[i + 1] - x
        return op