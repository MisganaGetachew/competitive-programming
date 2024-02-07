class Solution:
    def freqAlphabets(self, s: str) -> str:
        index = len(s) - 1
        ans = ""

        while index >= 0:
            if s[index] == "#":
                temp = int(s[index-2:index])
                ans += chr(temp + 96)
                index -= 3
            else:
                ans += chr(int(s[index]) + 96)
                index -= 1

        return ans[::-1]

            
     