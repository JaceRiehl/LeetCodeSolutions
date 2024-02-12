class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        s = list(s)
        vowels = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O', 'u', 'U']
        i, j = 0, len(s)-1
        while i < j:
            if s[i] not in vowels:
                i += 1
            if s[j] not in vowels:
                j -=1
            if s[i] in vowels and s[j] in vowels:
                s[j], s[i] = s[i], s[j]
                i += 1
                j -= 1
        return "".join(s)