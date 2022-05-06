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