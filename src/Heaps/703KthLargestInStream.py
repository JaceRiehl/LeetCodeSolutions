from collections import heapq
class KthLargest(object):

    def __init__(self, k, nums):
        """
        :type k: int
        :type nums: List[int]
        """
        self.minHeap = nums
        heapq.heapify(nums)
        self.k = k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap) 

    def add(self, val):
        """
        :type val: int
        :rtype: int
        """
        if len(self.minHeap) >= self.k:
            heapq.heappushpop(self.minHeap, val)
        else:     
            heapq.heappush(self.minHeap, val)
        return self.minHeap[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)