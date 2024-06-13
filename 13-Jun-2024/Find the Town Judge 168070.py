# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

from collections import defaultdict
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusted = [0 for i in range(n + 1)]
        for edge in trust:
            trusted[edge[0]] -= 1
            trusted[edge[1]]  += 1
        print(trusted)
        for i in range(1, len(trusted)):
            if trusted[i]  == n - 1:
                    return i
        return - 1
                
    

       
       
        