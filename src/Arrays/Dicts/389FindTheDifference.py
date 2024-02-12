class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        dic1 = Counter(s)
        dic2 = Counter(t)
        
        for i in dic2:
            if i not in dic1 or dic2[i] != dic1[i]:
                return i