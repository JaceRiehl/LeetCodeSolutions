class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            one = heapq.heappop(stones)
            two = heapq.heappop(stones)
            if one - two != 0:
                heapq.heappush(stones, one - two)
        return abs(stones[0]) if stones else 0