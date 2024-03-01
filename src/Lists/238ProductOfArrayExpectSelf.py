class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1] * len(nums)

        forward = 1
        # compute forward
        for i in range(len(nums)):
            res[i] = forward
            forward *= nums[i]

        backwards = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= backwards
            backwards *= nums[i]
        return res