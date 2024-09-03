# Problem: Single Number III - https://leetcode.com/problems/single-number-iii/

class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        dec = {}
        for num in nums:
            if num in dec:
                dec[num] += 1
            else:
                dec[num] = 1
        return [key for key, val in dec.items() if val == 1]