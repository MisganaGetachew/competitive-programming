# Problem: 3Sum - https://leetcode.com/problems/3sum/description/

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = set()   
        tar = 0    
        for x in range(len(nums)):
            left = x + 1
            right = len(nums) - 1  
            while left < right:
                if nums[left] + nums[right] + nums[x] > tar:
                        right -= 1
                elif nums[left] + nums[right] + nums[x] < tar:
                        left += 1
                else:
                    ans.add((nums[x], nums[left], nums[right]))
                    left += 1 
                    right -= 1    

        return ans