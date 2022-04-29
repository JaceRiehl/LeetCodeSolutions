"""
Leetcode 16 3SumClosest
Uses a similar strategy to 3Sum. 
It takes out some of the duplicate tracing that 3Sum was using and instead just looks for the pair closest to the target.

"""

def threeSumClosest(nums, target: int) -> int:
    nums.sort()
    closestPair = -1000
    for i, num in enumerate(nums):
        
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if abs(num + nums[l] + nums[r] - target) < abs(closestPair - target):
                closestPair = num + nums[l] + nums[r]
                print([num, nums[l], nums[r]])
            if num + nums[l] + nums[r] < target:
                l += 1
            elif num + nums[l] + nums[r] > target:
                r -= 1
            else: 
                return closestPair
            
    return closestPair

print(threeSumClosest([-1,0,1,2,-1,-4], 4))