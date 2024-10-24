# Problem: Count Primes - https://leetcode.com/problems/count-primes/

from math import isqrt 
class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 2:
           nums = []
          
        else:
           nums = [True] * (n)
           nums[0] = False
           nums[1] = False
        for i in range(2, isqrt(n)+ 1):
            if nums[i] == True:
                for j in range(i*i, n, i ):
                    nums[j] = False

        num = [i for i in range(len(nums)) if nums[i] == True]
        return len(num)
