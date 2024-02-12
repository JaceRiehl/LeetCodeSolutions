class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums1 = set(nums1) 
        nums2 = set(nums2)
        ret = []
        for num in nums1:
            if num in nums2:  
                ret.append(num)
        return ret