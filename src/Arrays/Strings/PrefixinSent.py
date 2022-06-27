
def isPrefixOfWord(sentence: str, searchWord: str) -> int:
    strs = sentence.split()
    length = len(searchWord)
    for i, word in enumerate(strs):
        if searchWord == word[:length]:
            return i+1
    return -1

print(isPrefixOfWord("i love cheeseburgers", "lo"))