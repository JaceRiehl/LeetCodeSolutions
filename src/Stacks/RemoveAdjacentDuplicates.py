"""
Leetcode 1047 RemoveAdjacentDuplicates

Technique:
- Use a stack to keep track of the most recent character that hasnt been deleted and then create a new string with the leftover characters.

"""

def removeDuplicates(s: str) -> str:
    stack = []
    res = ""
    for c in s:
        if stack and stack[-1] == c:
            stack.pop()
            continue
        stack.append(c)
    
    for c in stack:
        res += c
        
    return res
    
print(removeDuplicates("abcdeefgergfe"))