class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        return self.add_strs_to_hash(s) == self.add_strs_to_hash(t)

    def add_strs_to_hash(self,st):
        dic = {}
        for i in range(len(st)):
            if st[i] in dic:
                dic[st[i]] += 1
            else:
                dic[st[i]] = 1
        return dic

# Less efficent more boring approach
class Solution2:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)