# Problem: Additive Number - https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        n = len(num)
        curr = []
        def rec(i):
            m = len(curr)
            if i >= n:
                for j in range(2, m):
                    if curr[j] != curr[j - 2] + curr[j - 1]:
                        return False
                return m >= 3

            for idx in range(i, n):
                s = num[i:idx + 1]
                if len(s) > 1 and s[0] == "0":
                    return False
                val = int(s)
                if m <= 2 or val == curr[-2] + curr[-1]:
                    curr.append(val)
                    if rec(idx + 1):
                        return True
                    curr.pop()
            return False
        return rec(0)
