# Problem: Valid Parentheses - https://leetcode.com/problems/valid-parentheses

class Solution:
    def isValid(self, s: str) -> bool:
        if not s:
            return True
        ans = []
        d = {'(': ')', '{': '}', '[' : ']'}
        for i in s:
            if i in d:
                ans.append(i)
               
            else:
                if not ans or d[ans.pop()]  != i:
                    return False
                
               
        return not ans