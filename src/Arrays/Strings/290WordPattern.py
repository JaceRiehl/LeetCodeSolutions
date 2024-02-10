class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        strs = s.split(" ")
        if len(strs) != len(pattern):
            return False

        patternDict = {}
        strsDict = {}
        for i in range(len(strs)):
            if (pattern[i] in patternDict and patternDict[pattern[i]] != strs[i]) or (strs[i] in strsDict and strsDict[strs[i]] != pattern[i]):
                return False
            patternDict[pattern[i]] = strs[i]
            strsDict[strs[i]] = pattern[i]
        return True