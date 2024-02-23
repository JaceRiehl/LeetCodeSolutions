class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """

        l,r = 1, max(piles)
        ret = r
        while l <= r:
            k = (r + l) // 2
            hours = 0
            for pile in piles:
                f = float(pile) / float(k)
                hours += math.ceil(f)
            if hours <= h:
                ret = min(ret, k)
                r = k - 1
            else:
                l = k + 1
        return ret