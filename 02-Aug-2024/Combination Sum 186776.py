# Problem: Combination Sum - https://leetcode.com/problems/combination-sum/

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def solve(i, cur, total):
            if target == total:
                ans.append(cur.copy())
                return
            if i >= len(candidates) or target < total:
                return
            
            cur.append(candidates[i])
            solve(i, cur, total + candidates[i])
            cur.pop()
            solve(i+1, cur, total)
        solve(0,[],0)

        return ans