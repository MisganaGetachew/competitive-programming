# Problem: Remove Stones to Minimize the Total - https://leetcode.com/problems/remove-stones-to-minimize-the-total/

class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        maxheap = [-p for p in piles]
        heapq.heapify(maxheap)
        ttl = 0
        for i in range(k):
            lrg = - heapq.heappop(maxheap)
            val = lrg - math.floor(lrg/2)
            ttl += val
            heapq.heappush(maxheap, -val)
        return -sum(maxheap)


     

