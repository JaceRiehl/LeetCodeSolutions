from collections import Counter

# nlogn time n space
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        ret = []
        dic = Counter(nums)
        dic2 = sorted([(dic[key], key) for key in dic], reverse=True)
        
        for i in range(k):
            ret.append(dic2[i][1])
        return ret

# n time n space
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        frequency = [[] for i in range(len(nums)+1)]
        dic = {}
        ret = []

        for i in nums:
            dic[i] = 1 + dic.get(i, 0)
        
        for i in dic:
            frequency[dic[i]].append(i)

        i = len(frequency)-1
        while len(ret) != k:
            if frequency[i]:
                ret.extend(frequency[i][:k-len(ret)])
            i -= 1
        return ret