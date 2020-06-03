" Remove Duplicates from Sorted Array "

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        set_nums=list(set(nums))
        set_nums.sort()
        
        for i,element in enumerate(set_nums,0):
            nums[i]=element
        
        return len(set_nums)
            
        
