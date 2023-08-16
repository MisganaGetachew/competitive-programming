class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        longest = 0
        s = list(s)
        for left in range(len(s)):
            right = left + 1
            while right < len(s) and s[right] not in s[left:right]:
                    right += 1
            length = right - left
            if length > longest:
                    longest = length 
        return longest
