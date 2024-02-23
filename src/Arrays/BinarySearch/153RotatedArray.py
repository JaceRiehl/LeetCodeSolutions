class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l,r = 0, len(nums) - 1
        ret = nums[0]

        while l <= r:
            ret = min(ret, nums[l])
            m = (l+r) // 2
            if nums[m] >= nums[l]:
                l = m + 1
            else:
                r = m
            
        
        return ret