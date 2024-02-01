class Solution:
    def searchRange(self, nums, target: int):
        
        return [self.modifiedBinSearch(nums, target, True), self.modifiedBinSearch(nums, target, False)]

    def modifiedBinSearch(self,nums, target, findLeft):
        l,r = 0, len(nums)-1
        actualIndex = -1
        while l<=r:
            m = (r + l) // 2
            if target < nums[m]:
                r = m - 1
            elif target > nums[m]:
                l = m + 1
            else:
                actualIndex = m
                if findLeft:
                    r = m - 1
                else:
                    l = m + 1
        return actualIndex
