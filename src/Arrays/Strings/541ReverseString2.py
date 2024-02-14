# logic: tried to do this without just using pythons reverse string logic such as string[i:i+k] = reversed(string[i:i+k])
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        string = list(s)
        if len(string) <= 1:
            return s
        i = 0
        while i < len(string):
            index = i
            if i + k-1 >= len(string):
                j = len(string)-1
            else: 
                j = i + k-1
            while index < j:
                string[index], string[j] = string[j], string[index]
                index += 1
                j -= 1
            i += 2*k
        
        return "".join(string)