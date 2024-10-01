# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        length = (n - 1) * 2  
        
        cycle = time % length
        
        if cycle < n:
                 return cycle + 1
        else:
            return n - (cycle - (n - 1))
