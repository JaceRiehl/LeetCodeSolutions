"""
Leetcode 22 Valid Parentheses

Technique:
- Use a stack to keep track of the most recent start and a dictionary to check what a corresponding end is to a start.

"""

def isValid(s: str):
    endToStart = {
        "}": "{",
        "]": "[",
        ")": "(",
    }
    stack = []
    for c in s:
        if c in endToStart:
            
            if stack and stack.pop() == endToStart[c]:
                continue
            else:
                return False
        else:
            stack.append(c) 
    return True if not stack else False

print(isValid("[][[]]"))