class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
            s = ""
            strs = sorted(strs)
            first = strs[0]
            last = strs[-1]
            
            for char in range(min(len(first), len(last))):
                if first[char] != last[char]:
                    return s
                else:
                    s += first[char]
            return s