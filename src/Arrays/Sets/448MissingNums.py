class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        dic = set(nums)
        ret = []
        for i in range(1,len(nums)+1):
            if i not in dic:
                ret.append(i)
        return ret