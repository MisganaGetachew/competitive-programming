# Problem: Binary Number with Alternating Bits - https://leetcode.com/problems/binary-number-with-alternating-bits/

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b = bin(n)[2:]
        for i in range(1, len(b)):
            if b[i] == b[i-1]:
                return False
        return True