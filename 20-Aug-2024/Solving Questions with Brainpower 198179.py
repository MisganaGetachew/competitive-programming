# Problem: Solving Questions with Brainpower - https://leetcode.com/problems/solving-questions-with-brainpower/

class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        n = len(questions)
        dp = [0] * (n + 1)  
        for i in range(n - 1, -1, -1):
            points, brainpower = questions[i]
            next_question = i + brainpower + 1
            if next_question < n:
                dp[i] = max(points + dp[next_question], dp[i + 1])
            else:
                dp[i]=max(points, dp[i+1])
        
        return dp[0]

            