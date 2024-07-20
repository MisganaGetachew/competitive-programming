# Problem: Find K Pairs with Smallest Sums - https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/

import heapq
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k <= 0:
            return []

        min_heap = []
        ans = []
        
        # Push the first element of nums1 with every element of nums2 into the heap
        for j in range(min(k, len(nums2))):
            heapq.heappush(min_heap, (nums1[0] + nums2[j], 0, j))
        
        while k > 0 and min_heap:
            sum_val, i, j = heapq.heappop(min_heap)
            ans.append([nums1[i], nums2[j]])
            k -= 1
            
            # If there is a next element in nums1, push it into the heap
            if i + 1 < len(nums1):
                heapq.heappush(min_heap, (nums1[i + 1] + nums2[j], i + 1, j))
        
        return ans
