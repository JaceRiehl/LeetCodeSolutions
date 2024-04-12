class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = max(nums)
        ret = -1
        for i in range(len(nums)):
            if nums[i] != largest and nums[i] * 2 > largest:
                return -1
            if nums[i] == largest:
                ret = i
        return ret
    
# I realized its slightly faster to pop the index of the largest out of the array
class Solution(object):
    def dominantIndex(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        largest = max(nums)
        ret = nums.index(largest)
        nums.pop(ret)
        for i in range(len(nums)):
            if nums[i] * 2 > largest:
                return -1
            
        return ret