# Problem: Permutations - https://leetcode.com/problems/permutations/

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        ans = []

        def backtrack(unproc, proc):
            if not unproc:
                ans.append(proc)
                return 
            
            for i in range(len(unproc)):
                backtrack(unproc[:i] + unproc[i + 1:], proc + [unproc[i]])
        backtrack(nums, [])
        return ans


    