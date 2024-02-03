class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        
        good_pair = 0 
        for left in range(len(nums)):
            for right in range(left, len(nums)):
                if nums[left] == nums[right] and left < right:
                    good_pair += 1
        return good_pair
