from collections import Counter
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dic = Counter(s)
        ret = -1
        for i in range(len(s)):
            if dic[s[i]] == 1:
                return i
        return ret