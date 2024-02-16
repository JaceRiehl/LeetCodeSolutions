class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}

        for s in strs:
            count = [0] * 26
            for character in s:
                count[ord(character) - ord('a')] += 1
            counts = tuple(count)
            if counts not in res:
                res.update({counts: [s]})
            else:
                res[counts].append(s)

        ret = [res[key] for key in res]
        return ret
    
# with just sorting
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}

        for s in strs:
            key = str(sorted(s))
            if key not in res:
                res[key] = [s]
            else:
                res[key].append(s)


        ret = [res[key] for key in res]
        return ret