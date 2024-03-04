class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        window = set()
        l = 0

        for r in nums:
            if r in window:
                return True
            window.add(r)
            if len(window) > k:
                window.remove(nums[l])
                l += 1
        return False