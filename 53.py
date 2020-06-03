"  Maximum Subarray "

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)<1:
            return 0
        gmax=lmax=nums[0]
        for i in range(1,len(nums)):
            lmax=max(nums[i],lmax+nums[i])
            gmax=max(gmax,lmax)
        return gmax

