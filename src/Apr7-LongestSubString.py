"""
LeetCode Problem #3 Longest non repeating substring
Uses the sliding window that increases to the right with each pass and when we get a repeated character the window shrinks from the left.
We keep track of the highest non repeated window.
"""

def lengthOfLongestSubstring(s: str) -> int:
        setty = set()
        l = 0
        largestSubstr = 0
        for r in range(len(s)):
            while s[r] in setty:
                setty.remove(s[l])
                l += 1
            setty.add(s[r])
            largestSubstr = max(largestSubstr, r-l+1)
        return largestSubstr
    
print(lengthOfLongestSubstring("pwwkew"))


