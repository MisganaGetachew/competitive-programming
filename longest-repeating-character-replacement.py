class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        dic = {}
        max_len = 0
        maxLength = 0


        for right in range(len(s)):

            if s[right] in dic:
                dic[s[right]] += 1
            else:
                dic[s[right]] = 1

            max_len = max(max_len, dic[s[right]]) 

            while (right - left + 1 ) - max_len > k:
                dic[s[left]] -= 1
                if dic[s[left]] == 0:
                    del dic[s[left]]
                left += 1

            maxLength = max(maxLength, right - left + 1)

        return maxLength
            
