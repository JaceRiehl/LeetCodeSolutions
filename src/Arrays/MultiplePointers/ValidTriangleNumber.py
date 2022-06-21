def triangleNumber(nums) -> int:
    # i <= j < k
    # i+j > k
    nums.sort()
    
    ret = 0
    for k in range(2, len(nums)):
        i,j = 0, k-1
        while i < j:
            if nums[i] + nums[j] > nums[k]:
                ret += j-1
                j -= 1
            else:
                i+= 1
    
    return ret

print(triangleNumber([2,2,3,4]))