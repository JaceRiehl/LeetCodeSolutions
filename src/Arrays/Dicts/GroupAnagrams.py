def groupAnagrams(strs):
    dic = {}
    res = []
    for word in strs:
        sortedWord = sorted(word)
        sortedWord= "".join(sortedWord)
        if sortedWord in dic:
            dic[sortedWord].append(word)
        else:
            dic[sortedWord] = [word]
    for val in dic.values():
        res.append(val)
    return res


print(groupAnagrams(["eat","tea","tan","ate","nat","bat"]))