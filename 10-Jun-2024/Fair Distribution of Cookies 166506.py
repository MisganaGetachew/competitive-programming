# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        childs = [0] * k
        unfair = inf
        def backtrack(idx):
            nonlocal childs, unfair

            if idx == len(cookies):
                unfair = min(unfair, max(childs))
                return 
            if unfair <= max(childs):
                return 

            for i in range(k):
                childs[i] += cookies[idx]
                backtrack(idx + 1)
                childs[i] -= cookies[idx]
        backtrack(0)
        return unfair

    