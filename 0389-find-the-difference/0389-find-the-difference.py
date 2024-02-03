class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        st = []
        left = 0
        s = sorted(s)
        t = sorted(t)
        
        for char in t:
            if left < len(s) and char == s[left] :
                left += 1
            else:
                st.append(char)
        return "".join(st)
            
            