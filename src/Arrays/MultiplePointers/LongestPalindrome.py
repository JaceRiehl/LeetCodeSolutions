"""
Leetcode Problem #5 LongestPalindrome
Theres a few edge cases we have to consider here
By going from the current character and looking outwards from each side we save a lot of time:
For even cases like aba, if were at b our pointers look like this: b - aba
Theres also even cases we have to worry about like abba. in this case we have to increment the right pointer by 1 and do the same process so that its evaluating bb abba
"""


def longestPalindrome(s: str) -> str:
    longestPalindrome = 0
    res = ""
    
    for i in range(len(s)):
        # Odd cases
        l,r = i, i
        res, longestPalindrome = compute_palindromes(s,l,r,res,longestPalindrome)
   
        # Even Cases
        l,r = i, i+1
        res, longestPalindrome = compute_palindromes(s,l,r,res,longestPalindrome)
        
        
    return res
    
    
    
def compute_palindromes(s, l, r, res, longestPalindrome):
    while l >= 0 and r < len(s) and s[l] == s[r]:
        if (r - l + 1) > longestPalindrome:
            res = s[l:r+1]
            longestPalindrome = r - l + 1
        l -= 1 
        r += 1
    return res, longestPalindrome
print(longestPalindrome("abcbafdsfwefeabbbbbbbbba"))