# Problem: Peak Index in a Mountain Array - https://leetcode.com/problems/peak-index-in-a-mountain-array/

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        
        mx = -inf
        dx = 0
        for val in arr:
            if val > mx:
                mx = val
                # dx = idx
                # print(dx)
        for idx, val in enumerate(arr):
            if val == mx :
                return idx
                
        
