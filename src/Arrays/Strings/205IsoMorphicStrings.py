class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        hashSetS = {}
        hashSetT = {}

        for i in range(len(s)):
            s1, t1 = s[i], t[i]
            if (s1 in hashSetS and hashSetS[s1] != t1) or (t1 in hashSetT and hashSetT[t1] != s1):
                return False

            hashSetS[s[i]] = t[i]
            hashSetT[t[i]] = s[i]

        return True
        