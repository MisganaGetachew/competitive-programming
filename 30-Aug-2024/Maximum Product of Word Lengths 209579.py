# Problem: Maximum Product of Word Lengths - https://leetcode.com/problems/maximum-product-of-word-lengths/

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        sets = [set(word) for word in words]
        max_ = 0

        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
               
                if not (sets[i] & sets[j]):
                    max_ = max(max_, len(words[i]) * len(words[j]))

        return max_
