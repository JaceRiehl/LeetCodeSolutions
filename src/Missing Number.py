""" LeetCode 268.Missing Number
You are given a list of n-1 size and are asked to find the missing number.

This is the solution for O(1) space and O(n)

Edge Cases:
No edge cases
"""

def missingNumber(nums):
        result = len(nums)
        
        for i in range(len(nums)):
            result += i - nums[i]
            
        return result