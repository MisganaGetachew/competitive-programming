class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        Ssorted = sorted(s)
        Tsorted = sorted(t)
        if Ssorted == Tsorted:
            return True
        else:
            return False
