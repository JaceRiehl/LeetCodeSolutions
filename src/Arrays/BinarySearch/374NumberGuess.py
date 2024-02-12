# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        start = 0
        while start <= n:
            res = (n + start) // 2
            ret = guess(res)
            if ret == 1:
                start = res + 1
            elif ret == -1:
                n = res - 1
            else:
                return res