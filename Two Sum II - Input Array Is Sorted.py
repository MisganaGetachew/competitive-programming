class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        # example array = [2,7,11,15], target = 9
        arr = []
        right = len(numbers)
        left = 1
        numbers.insert(0, 0)
        for i in range(1,len(numbers)):
            if left < right:
                    temp  = numbers[left] + numbers[right]
                    if temp < target:
                        left += 1
                    elif temp > target:
                        right -= 1
                    else:
                        arr.append(left)
                        arr.append(right)
                        break
                        
        return arr
            
