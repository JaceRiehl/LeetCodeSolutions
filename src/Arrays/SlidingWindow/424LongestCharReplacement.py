class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        dic = {}
        longestSub = 0
        
        for r in range(len(s)):
            dic[s[r]] = 1 + dic.get(s[r], 0)
            highestChar = max(dic.values())
            if (r - l + 1) - highestChar > k:
                dic[s[l]] -= 1
                l += 1
            
            longestSub = max(longestSub, r-l+1)
            
        return longestSub