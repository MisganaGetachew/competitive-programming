# Problem: Longest Nice Substring - https://leetcode.com/problems/longest-nice-substring/

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        
        ans = ""
        def rec(s):
            nonlocal ans
            sett = set(s)
            for i in range(len(s)):
                if s[i].lower() not in sett or s[i].upper() not in sett:
                    left = s[:i]
                    right = s[i+1:]
                    lefts = rec(left)
                    rights = rec(right)
                    # if rec(left):
                    #     lefts += left
                    # if rec(right):
                    #     rights += right
                    ans = max(lefts, rights, key = len)
                    print()
                    return ans
            return s
        
        return  rec(s)

