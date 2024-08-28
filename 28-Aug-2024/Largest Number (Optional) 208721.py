# Problem: Largest Number (Optional) - https://leetcode.com/problems/largest-number/

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
       
        ans = list(map(str, nums))
        
        for i in range(len(ans)):
            for j in range(i + 1, len(ans)):
                if ans[i] + ans[j] < ans[j] + ans[i]:
                    ans[i], ans[j] = ans[j], ans[i]
        
        res = ''.join(ans)
        
        if res[0] == '0':
            return '0'
        else:
            return res