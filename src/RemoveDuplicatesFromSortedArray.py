"""
Leetcode 26 Removing duplicates from a sorted array
This is going to use the fast and slow pointer strategy, 

O(n) time
O(1) space

"""


def removeDuplicates(nums) -> int:
    l,r = 1, 1
    while r < len(nums):
        if nums[r] != nums[r-1]:
            nums[l] = nums[r]
            l+=1
        r+=1
    return l
    
print(removeDuplicates([1,2,3,3,4,4,5,5,5,5,5,6]))