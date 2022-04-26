"""
Leetcode 15 

Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

Uses a recursive backtracking algorithm type approach where it will continually breakdown the numbers. 
For instance, if you have 2,3 it will take a from 2 and call the recursive function on every character from 3. so 'ad' 'ae' 'af' then move on to b from 2....

No Edge cases
"""

def letterCombinations(digits: str):
    res = []
    numbers = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    

    def backtrack(i, currentStr):
        if len(currentStr) == len(digits):
            res.append(currentStr)
            return
        
        for character in numbers[digits[i]]:
            backtrack(i+1, currentStr + character)
        
    if digits:
        backtrack(0, "")
    return res
    
print(letterCombinations("23"))