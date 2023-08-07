class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_number = 0
        for i in range(len(nums)+1):
            if i not in nums:
                missing_number = i
        return missing_number
