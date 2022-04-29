"""
Leetcode 15 3Sum
Uses a similar strategy to twosum2. It adds another loop to go through the first number and then uses twosum2 strat to get the other two numbers.

"""

def threeSum(nums):
    ret = []
    nums.sort()
    
    for i, num in enumerate(nums):
        if i > 0 and num == nums[i-1]:
            continue
        
        l = i + 1
        r = len(nums) - 1
        while l < r:
            if num + nums[l] + nums[r] < 0:
                l += 1
            elif num + nums[l] + nums[r] > 0:
                r -= 1
            else: 
                ret.append([num, nums[l], nums[r]])
                l+=1
                while nums[l] == nums[l -1] and l < r:
                    l += 1
    return ret

print(threeSum([-1,0,1,2,-1,-4]))
        