"""
Leetcode problem #1 Two Sum
Uses a dictionary to keep track of the numbers weve gone over and if the target - the current number is in the dictionary we have a match
"""


# Solution 1 : 2 pointers - not a great solution because the array doesnt come in sorted
# def twoSum(nums, target):
#     nums2 = nums.copy()
#     nums2.sort()
#     l = 0
#     r = len(nums2) -1
#     while l < r: 
#         if nums2[l] + nums2[r] < target:
#             l += 1
#         elif nums2[l] + nums2[r] > target:
#             r -= 1
#         else:
#             if nums2[l] == nums2[r]: 
#                 ar = [nums.index(nums2[l]), nums.index(nums2[r], l+1, len(nums2))]
#             else: ar = [nums.index(nums2[l]), nums.index(nums2[r])]
#             ar.sort()
#             return ar
            
# Solution 2 : using a dictionary
def twoSum(nums, target):
    dict = {}
    for i, num in enumerate(nums):
        if num in dict:
            return [dict[num],i]
        else:
            dict[target - num] = i
    return []
            
arr = twoSum([5,75,25], 100)

print(arr)