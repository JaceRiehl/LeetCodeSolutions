class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        for i in ransomNote:
            if i not in magazine:
                return False
            else:
                magazine = magazine.replace(i, " ", 1)

        return True