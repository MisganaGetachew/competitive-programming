class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        newnums = set(nums)
        for i in range(len(nums) + 1):
            if i not in newnums:
                return i
            