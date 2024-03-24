class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        complete = 0
        i = 0
        while complete < n:
            i += 1
            complete += i 
        return i if complete == n else i - 1