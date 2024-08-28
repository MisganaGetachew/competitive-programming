# Problem: Number Complement - https://leetcode.com/problems/number-complement/

class Solution:
    def findComplement(self, num: int) -> int:
        print(bin(num))
        ans = ""
        for i in bin(num)[2:]:
            if i == "1":
                ans += "0"
            else:
                ans += "1"
        return int(ans, 2)