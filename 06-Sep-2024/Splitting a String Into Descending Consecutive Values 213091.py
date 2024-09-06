# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def solve(value,index):
            if index == len(s):
                return True
            for j in range(index, len(s)):
                val = int(s[index:j+1])
                if val + 1 == value and solve(val, j + 1):
                    return True
            return False
        
        for i in range(len(s)-1):
            val = int(s[:i+1])
            if solve(val, i+1):
                return True
        return False


        

        