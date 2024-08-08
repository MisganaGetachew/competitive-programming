# Problem: 0 -  1 Knapsack - https://www.geeksforgeeks.org/problems/0-1-knapsack-problem0945/1

import collections
class Solution:
    
    #Function to return max value that can be put in knapsack of capacity W.
    def knapSack(self,W, wt, val, n):
        memo = collections.defaultdict(int)
        
        def dp(idx, capacity):
            
            if idx >= n or capacity <= 0:
                return 0
                
            if (idx, capacity) not in memo:
                include = 0
                if wt[idx] <= capacity:
                    include = val[idx] + dp(idx + 1, capacity-wt[idx])
                
                exclude = dp(idx + 1, capacity)
                memo[(idx, capacity)] = max(include, exclude)
                
            return memo[(idx, capacity)]
            
        return dp(0, W)