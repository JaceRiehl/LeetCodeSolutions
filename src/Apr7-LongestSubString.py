# Sliding window
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


