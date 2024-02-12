from collections import Counter

class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        dic_1 = Counter(nums1)
        dic_2 = Counter(nums2)
        ret = []

        for i in dic_1:
            if i in dic_2:
                ret += [i] * min(dic_1[i],dic_2[i])
        return ret