def jump(nums) -> int:
    l,r = 0,0
    res = 0
    while r < len(nums)-1 :
        longest_jump = 0
        for i in range(l,r+1):
            longest_jump = max(longest_jump, i+nums[i])
        l = r+1
        r = longest_jump
        res+=1
    return res
print(jump([2,3,0,1,4]))
