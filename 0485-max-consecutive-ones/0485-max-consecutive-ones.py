class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
            temp = 0
            count = 0
            for num in nums :
                if num == 1:
                    temp += 1
                    count = max(temp, count)    
                else:
                    temp = 0
            return count