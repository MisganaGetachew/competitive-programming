# Problem: K Items With the Maximum Sum - https://leetcode.com/problems/k-items-with-the-maximum-sum/

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        else:
            temp = k - numOnes
            if temp <= numZeros:
                return numOnes
            else:
                return numOnes - (temp - numZeros)
            # temp = k - numOnes = 7 
            # temp = 7 > 6(numZeros) we need the difference
            # diff = 1 meaning we need to decrease by 1 


            
            