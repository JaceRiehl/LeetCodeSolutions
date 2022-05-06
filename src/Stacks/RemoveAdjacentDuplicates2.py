"""
Leetcode 1209 RemoveAdjacentDuplicates2

Technique:
- Use a stack to keep track of the most recent character that hasnt been deleted and then create a new string with the leftover characters.

"""

def removeDuplicates(s: str, k) -> str:
    stack = []
    res = ""
    
    for c in s:
        if stack and stack[-1][0] == c:
            stack[-1][1] += 1
            if stack[-1][1] == k:
                stack.pop()
            continue
        stack.append([c,1])
    
    for c in stack:
        res += c[0] * c[1]
        
    return res
    
print(removeDuplicates("deeedbbcccbdaa", 3))