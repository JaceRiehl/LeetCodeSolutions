class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        ret = 0
        l,r = 0,len(nums)-1

        while l <= r:
            if nums[r] == val:
                r -= 1
                ret += 1
            elif nums[l] == val:
                nums[r], nums[l] = nums[l], nums[r]
                ret += 1
                r -= 1
                l += 1
            else:
                l += 1
        
        return len(nums) - ret