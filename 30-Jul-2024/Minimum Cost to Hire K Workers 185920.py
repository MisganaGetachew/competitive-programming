# Problem: Minimum Cost to Hire K Workers - https://leetcode.com/problems/minimum-cost-to-hire-k-workers/description/

class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        res = inf
        pair = []
        for i in range(len(quality)):
            pair.append((wage[i]/quality[i], quality[i]))
        pair.sort(key =lambda x: x[0])
        mx_heap = []
        ttl = 0
        for rate, q in pair:
            heapq.heappush(mx_heap, -q)
            ttl += q
            if len(mx_heap) > k:
                ttl += heapq.heappop(mx_heap)
            if len(mx_heap) == k:
                res = min(res, ttl * rate)
        return res