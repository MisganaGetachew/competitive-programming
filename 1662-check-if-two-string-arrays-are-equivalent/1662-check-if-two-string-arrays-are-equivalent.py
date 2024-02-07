class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        st1 = "".join(word1)
        st2 = "".join(word2)
        if st1 == st2: 
            return True
        return False
            