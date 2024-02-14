class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret = []
        dic = Counter(nums)
        doubleNum = 0
        missingNum = 0
        for i in range(1,len(nums)+1):
            if i not in dic:
                missingNum = i
            if dic[i] == 2:
                doubleNum = i
            
        return [doubleNum,missingNum]