class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        left = 0
        right = 0
        temp_sum = 0
        min_len = float('inf')
        while right < len(nums):
            temp_sum += nums[right]
            right += 1
            while left <= right and temp_sum >= target:
                min_len = min(min_len, right - left)
                temp_sum -= nums[left]
                left += 1
        if min_len == float('inf'):
            return 0
        else:
            return min_len
