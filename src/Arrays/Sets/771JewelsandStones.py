class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        jewelsDict = set(jewels)
        ret = 0
        for item in stones:
            if item in jewelsDict:
                ret += 1
        return ret