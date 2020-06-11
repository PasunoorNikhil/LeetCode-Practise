" Remove Duplicates from Sorted Array II "

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        i, idx, j = 2, 2, len(nums)
        while i < j:
            if nums[i] != nums[idx - 1] or nums[i] != nums[idx - 2]:
                nums[idx] = nums[i]
                idx+=1
            i += 1
        return idx 
        
