# Problem: Longest Palindromic Substring - https://leetcode.com/problems/longest-palindromic-substring/

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""
        
        start = 0
        end = 0
        
        for c in range(2 * n - 1):
            l = c // 2
            r = l + c % 2
            
            while l >= 0 and r < n and s[l] == s[r]:
                if r - l > end - start:
                    start = l
                    end = r
                l -= 1
                r += 1
        
        return s[start:end + 1]