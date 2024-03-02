class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1: 
            return s
        
        ret = ""
        for row in range(numRows):
            increment = 2 * (numRows - 1)
            for i in range(row, len(s), increment):
                zigzagIndex = i + increment - (2 * row)
                ret += s[i]
                if (row > 0 and row < numRows -1 and zigzagIndex < len(s)):
                    ret += s[zigzagIndex]
        return ret