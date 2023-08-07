class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        length = len(nums)
        for n in range(0, length):
                for x in range(0, n):
                    if nums[n] + nums[x] == target:
                        return [n, x]


