class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        temp = []
        dic = {}
        for i in s:
            if i in dic:
                dic[i] += 1
            else:
                dic[i] = 1
        for key, value in dic.items():
            temp.append([key, value])


        
        temp.sort(key=lambda x: x[1], reverse=True)

        s = [i * k for i, k in temp]

        

        return "".join(s)
