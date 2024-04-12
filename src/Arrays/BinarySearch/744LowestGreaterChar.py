class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        """
        ret = letters[0]
        l,r = 0, len(letters)
        while l < r:
            m = (l + r) // 2
            if letters[m] > target:
                r = m
                ret = letters[m]
            else:
                l = m + 1
            
        return ret
