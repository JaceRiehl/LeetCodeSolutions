class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        ret = ""
        while columnNumber > 0:
            remainder = (columnNumber-1) % 26
            ret += chr(ord('A') + remainder)
            columnNumber = (columnNumber - 1) // 26

        return ret[::-1]