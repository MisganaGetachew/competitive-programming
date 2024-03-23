class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        left = 0
        right = n
        ans = []

        while right < len(nums) and left < n:
            ans.append(nums[left])
            ans.append(nums[right])
            right += 1
            left += 1
        return ans  