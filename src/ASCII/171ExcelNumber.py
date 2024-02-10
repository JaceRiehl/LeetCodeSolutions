class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        ret = 0
        multiplier = 1

        for i in range(len(columnTitle)-1, -1, -1):
            ret += (ord(columnTitle[i]) - 64) * multiplier
            multiplier *= 26

        return ret