class Solution(object):
    def repeatedSubstringPattern(self, s):
        """
        :type s: str
        :rtype: bool
        """
        sub = ""
        for r in range(len(s)//2):
            sub += s[r]
            if sub * (len(s) // len(sub)) == s:
                return True

        return False