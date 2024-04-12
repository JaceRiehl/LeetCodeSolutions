class Solution(object):
    def toLowerCase(self, s):
        """
        :type s: str
        :rtype: str
        """
        ret = ""

        for c in s:
            if ord(c) <= 90 and ord(c) >= 65:
                ret += chr(ord(c) + 32)
            else:
                ret += c
        return ret