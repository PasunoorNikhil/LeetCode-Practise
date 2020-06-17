" Minimum Value to Get Positive Step by Step Sum "

class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        minval,cursum=0,0
        for i in nums:
            cursum=i+cursum
            minval=min(minval,cursum)
        return abs(minval)+1
        
