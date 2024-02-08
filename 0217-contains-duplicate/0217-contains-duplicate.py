class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        num = set()
        for i in nums:
            if i in num:
                return True
            else:
                num.add(i)
        return False
            