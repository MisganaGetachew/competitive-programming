# Problem: Find Kth Bit in Nth Binary String - https://leetcode.com/problems/find-kth-bit-in-nth-binary-string/

class Solution:
    def findKthBit(self, n: int, k: int) -> str:
        def rec(n, k):
            if n == 1:
                return 0
            prev = n//2
            if k == prev + 1:
                return 1
            elif k <= prev:
                return rec(prev, k)
            else:
                return 1 - rec(prev, n - k + 1)
        length = (2 ** n) - 1
        return str(rec(length, k))
                
            

