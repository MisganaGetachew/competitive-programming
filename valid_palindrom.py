class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = []
        for i in s:
            if i.isalpha() or i.isdigit():
                temp.append(i.lower())
        s1 = "".join(temp)
        s2 = s1[::-1]
        if s1 == s2:
            return 'true'
