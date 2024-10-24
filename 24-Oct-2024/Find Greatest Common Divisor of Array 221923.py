# Problem: Find Greatest Common Divisor of Array - https://leetcode.com/problems/find-greatest-common-divisor-of-array/

class Solution:
    def findGCD(self, nums: List[int]) -> int:
        min_ = min(nums)
        max_ = max(nums)
        num = 1
        for i in range(1, min_ + 1):
            if min_ % i == 0 and max_ % i == 0:
                num = max(num, i)
        return num