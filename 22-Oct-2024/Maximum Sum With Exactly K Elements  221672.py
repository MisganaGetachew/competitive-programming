# Problem: Maximum Sum With Exactly K Elements  - https://leetcode.com/problems/maximum-sum-with-exactly-k-elements/description/

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        
        score = 0
        for _ in range(k):
            
            m = nums[-1]
            score += m
            nums[-1] = m + 1
            
            nums.sort()
        
        return score
