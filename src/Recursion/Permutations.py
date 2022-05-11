def permute(nums):
    result = []
    
    if len(nums) == 1:
        return [nums[:]]

    for i in range(len(nums)):
        n = nums.pop(0)

        permutations = permute(nums)

        for p in permutations:
            p.append(n)

        result.extend(permutations)
        nums.append(n)
    return result

print(permute([1,1,2]))