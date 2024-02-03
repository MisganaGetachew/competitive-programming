class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:

        left  = 0
        right = 0
        output = []
        

        for i in range(max(len(word1), len(word2))):
            if left < len(word1):
                output.append(word1[left])
                left += 1
            if right < len(word2):
                output.append(word2[right])
                right += 1

            
        return "".join(output)