# Problem: Peak Index in a Mountain Array - https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
         l = 0
         r = len(arr) - 1

         while l <= r:
            m = (l + r)//2
            if arr[m] > arr[m + 1]:
                r = m -1
            else:
                l = m + 1
         return l
