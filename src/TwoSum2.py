"""
Leetcode 167. Two Sum 2
Find the target in the array, expect its sorted.

No edge cases
"""

def twoSum(numbers, target):
    l = 0
    r = len(numbers) - 1
    
    while l < r:
        print(l,r)
        if numbers[l] + numbers[r] > target:
            r -= 1
        elif numbers[l] + numbers[r] < target:
            l += 1
        else: 
            return [l+1, r+1]
        
print(twoSum([1,2,3,4,8,9], 7))