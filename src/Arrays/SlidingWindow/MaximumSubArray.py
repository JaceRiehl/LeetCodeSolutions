def maxSubArray(nums):
    maxSum = nums[0]
    currentSum = 0
    for num in nums:
        if currentSum < 0:
            currentSum = 0
        currentSum += num
        if currentSum > maxSum:
            maxSum = currentSum
    return maxSum

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))