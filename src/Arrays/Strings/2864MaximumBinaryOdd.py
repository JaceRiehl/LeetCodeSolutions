class Solution(object):
    def maximumOddBinaryNumber(self, s):
        """
        :type s: str
        :rtype: str
        """
        ones = s.count('1')
        
        return "1" * (ones - 1) + "0" * (len(s) - ones) + "1"