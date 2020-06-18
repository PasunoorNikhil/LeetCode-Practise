" Find Pivot Index "

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        cursum=0
        totalsum=sum(nums)
        for i in range(len(nums)):
            if totalsum-cursum-nums[i]==cursum:
                return i
            cursum += nums[i]
        return -1

