# Problem: Top K Frequent Elements - https://leetcode.com/problems/top-k-frequent-elements/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        n = [[key, val] for key, val in freq.items()]
        n.sort(key=lambda x:x[1], reverse = True)
        print(freq)
        print(n)
        return [i for i, j in n[:k]]