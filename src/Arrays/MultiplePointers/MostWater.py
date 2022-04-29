"""
Leetcode 11 MostWater
You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i])

Solved this using the two pointer approach. 

"""


def maxArea(height) -> int:
    ret = 0
    l = 0
    r = len(height) - 1
    
    while l < r:
        minNum = min(height[l], height[r])
        dist = abs(l - r)
        area = minNum * dist
        ret = area if area > ret else ret
        if minNum == height[l]:
            l += 1
        else:
            r -= 1
        
    
    return ret
    
    
print(maxArea([1,8,6,2,5,4,8,3,7]))
    