
# More space O(n) (potentially based on how sorting algorithms are classed) but faster algorithm O(n)
def containsDuplicate(nums) -> bool:
    dupSet = set()
    
    for n in nums:
        if n in dupSet:
            return True
        dupSet.add(n)
        
    return False
    
    
print(containsDuplicate([1,2,3,1,2]))


# O(1) space O(n log n) time
def containsDuplicate2(nums) -> bool:
    l = 0
    nums.sort()
    for r in range(1,len(nums)):
        if nums[l] == nums[r]:
            return True
        l += 1
    return False

print(containsDuplicate2([1,2,3,1,2]))